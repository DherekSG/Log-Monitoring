# 🔍 Log Monitoring para GRC com Python

Este projeto tem como objetivo monitorar arquivos de logs (firewall, sistema ou segurança) e gerar **alertas de não conformidade** com base em regras definidas, como:

- Acessos fora do horário permitido
- Uso de portas proibidas
- Falhas de login repetidas

O projeto é ideal para portfólios de profissionais que desejam ingressar na área de **Governança, Riscos e Compliance (GRC)** ou **Segurança da Informação**.

---

## 🧠 Objetivo

Automatizar a análise de logs para identificar comportamentos suspeitos ou violações de políticas de segurança, simulando uma etapa básica de um processo de monitoramento de segurança (como em um SOC).

---

## 🧰 Tecnologias Utilizadas

- [Python 3.10+](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/) para análise de dados
- JSON para regras configuráveis
- Git + GitHub para controle de versão

---

## 🗂️ Estrutura do Projeto

```
    log-monitoring/
    ├── alerts/ # Arquivos de alertas gerados
    ├── configs/
    │ └── rules.json # Regras de monitoramento configuráveis
    ├── logs/
    │ └── sample_log.csv # Logs de exemplo
    ├── src/
    │ ├── main.py # Script principal
    │ ├── parser.py # Leitura e tratamento dos logs
    │ ├── rules_engine.py # Avaliação das regras
    │ ├── alert_manager.py # Geração e armazenamento de alertas
    │ └── utils.py # Funções auxiliares
    ├── requirements.txt # Dependências Python
    └── README.md # Documentação do projeto
```


---

## ⚙️ Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/dhereksg/log-monitoring.git
cd log-monitoring

Instale as dependências:

pip install -r requirements.txt

Edite as regras em configs/rules.json conforme necessário.
Execute o script principal:
python src/main.py

Os alertas serão salvos na pasta /alerts.
```

## 💡 Exemplos de Alertas Gerados
Usuário acessou o sistema às 03:00 da manhã (fora do horário permitido)

Acesso à porta 3389 detectado

Três falhas de login consecutivas pelo mesmo IP

## 🛡️ Boas Práticas Aplicadas
Modularização do código

Separação entre dados, regras e lógica

Reutilização de funções

Alertas salvos com timestamp

Estrutura pronta para futura integração com SIEM

## 🚀 Futuras Evoluções
Integração com e-mail ou Telegram para envio automático de alertas

Suporte a múltiplos formatos de log (JSON, syslog, Apache, etc.)

Interface web com Streamlit para visualizar os alertas

Pipeline CI/CD com GitHub Actions

Integração com S3 ou banco de dados para centralizar os logs

## 🤝 Contribuindo
Contribuições são bem-vindas! Se quiser colaborar com novas regras, parsers ou melhorias, basta abrir um PR ou criar uma issue.

## 👨‍💻 Autor
[Dherek S.G.](https://github.com/DherekSG)

Desenvolvedor full-stack | Estudante de Segurança da Informação

Foco em GRC, automações, cibersegurança e red team!

## [LinkedIn](https://www.linkedin.com/in/dherekschaberle/) • [GitHub](https://github.com/DherekSG)