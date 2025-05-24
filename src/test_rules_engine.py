import unittest
from datetime import datetime
from src.rules_engine import fora_do_horario, porta_proibida, detectar_falhas, salvar_alerta

class TestRulesEngine(unittest.TestCase):
    def setUp(self):
        
        self.tentativas_falha = {}
        self.alertas = []

    def test_fora_do_horario(self):
        
        registro = {"timestamp": "2025-05-22 09:30:00", "ip_address": "192.168.0.1"}
        resultado = fora_do_horario(registro)
        self.assertFalse(resultado)

       
        registro = {"timestamp": "2025-05-22 19:30:00", "ip_address": "192.168.0.1"}
        resultado = fora_do_horario(registro)
        self.assertTrue(resultado)

    def test_porta_proibida(self):
        registro = {"port": "23", "timestamp": "2025-05-23 10:00:00"}
        resultado = porta_proibida(registro)
        self.assertTrue(resultado)


        
        registro = {"port": "22"}
        resultado = porta_proibida(registro)
        self.assertTrue(resultado)

    def test_detectar_falhas(self):
        registro = {"ip_address": "192.168.0.12", "status": "failed", "timestamp": "2025-05-22 10:00:00"}

        
        for _ in range(3):
            detectar_falhas(registro, self.tentativas_falha, limite=3)

        self.assertEqual(self.tentativas_falha.get("192.168.0.12", 0), 0)  # Deve resetar após alerta

if __name__ == "__main__":
    unittest.main()
