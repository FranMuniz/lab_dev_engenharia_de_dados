## Laboratório de Desenvolvimento - Engenharia de Dados

Um laboratório completo para estudos em **Engenharia de Dados**, rodando via **Docker**.  
Aqui você encontra um ambiente integrado com **Spark, PySpark, Jupyter, PostgreSQL e Airflow**, pronto para treinar desde consultas SQL até orquestração de pipelines de dados.

### Tecnologias

- **Apache Spark** → processamento distribuído de dados.
- **PySpark** → API Python para manipulação de dados no Spark.
- **Jupyter Notebook** → ambiente interativo para experimentos.
- **PostgreSQL** → banco de dados relacional para integração com Spark e Airflow.
- **Apache Airflow** → orquestrador de workflows e pipelines de dados.

<p align="center">
  <img src="https://img.shields.io/badge/Spark-FF6F00?style=for-the-badge&logo=apachespark&logoColor=white"/>
  <img src="https://img.shields.io/badge/PySpark-EE4C2C?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Spark_SQL-FF6F00?style=for-the-badge&logo=apachespark&logoColor=white"/>
  <img src="https://img.shields.io/badge/Postgres-316192?style=for-the-badge&logo=postgresql&logoColor=white"/>
  <img src="https://img.shields.io/badge/Airflow-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white"/>
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white"/>
</p>

---

### 📌 Roadmap de Estudos

flowchart LR
    A[📌 Python] --> B[📌 SQL]
    B --> C[📌 Git & GitHub]
    C --> D[📌 Manipulação de Dados]
    D --> E[📌 Spark & PySpark]
    E --> F[📌 Airflow]
    F --> G[📌 PostgreSQL & Data Warehouses]
    G --> H[📌 Engenharia de Dados prática]
    H --> I[📌 Boas práticas & Soft Skills]
    I --> J[📌 Extras: Docker, CI/CD, Big Data]

    style A fill:#f9c74f,stroke:#000,stroke-width:1px
    style B fill:#90be6d,stroke:#000,stroke-width:1px
    style C fill:#f94144,stroke:#000,stroke-width:1px
    style D fill:#577590,stroke:#000,stroke-width:1px
    style E fill:#43aa8b,stroke:#000,stroke-width:1px
    style F fill:#f3722c,stroke:#000,stroke-width:1px
    style G fill:#90be6d,stroke:#000,stroke-width:1px
    style H fill:#577590,stroke:#000,stroke-width:1px
    style I fill:#f8961e,stroke:#000,stroke-width:1px
    style J fill:#f9844a,stroke:#000,stroke-width:1px

---

## 📂 Estrutura de Pastas

```bash
lab_dev_engenharia_de_dados/
│── .env                 # variáveis de ambiente
│── .gitignore           # arquivos/diretórios ignorados pelo Git
│── docker-compose.yml   # definição dos serviços
│── Dockerfile           # imagem customizada para o container
│── README.md            # documentação do projeto
│── notebooks/           # Jupyter Notebooks
│── dags/                # DAGs do Airflow
│── logs/                # logs do Airflow
│── plugins/             # plugins do Airflow
```
---

## Como rodar o ambiente

### 1️⃣ Clone este repositório
Clone o repositório e entre na pasta do projeto:  
**Comandos:**  
```bash
git clone git@github.com:FranMuniz/lab_dev_engenharia_de_dados.git 
cd lab_dev_engenharia_de_dados/
```

---

### 2️⃣ Configure o arquivo .env
### PostgreSQL
```
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin
POSTGRES_DB=mydb
```

### Jupyter (opcional, já está sem token)
```
JUPYTER_PASSWORD_HASH=CHAVE_HASH_AQUI
```

### Airflow
```
AIRFLOW_DB_USER=admin
AIRFLOW_DB_PASSWORD=admin
AIRFLOW_DB_NAME=airflow
AIRFLOW_FERNET_KEY=CHAVE_FERNET_AQUI
```
Gere a chave Fernet com:
```bash
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```

---

### 3️⃣ Suba os serviços com Docker Compose
**Comando:**  
```bash
docker-compose up -d
```

---

### 4️⃣ Acesse os serviços

**Spark Master**  
[http://localhost:8080](http://localhost:8080)  
Interface web do Spark para acompanhar workers e jobs.

**Spark Worker**  
[http://localhost:8081](http://localhost:8081)  
Interface web do worker conectado ao cluster Spark.

**Jupyter Notebook**  
[http://localhost:8888](http://localhost:8888)  
Ambiente interativo com PySpark já configurado.  
Não é necessário informar token ou senha para acessar.

**PostgreSQL**  
Host: `localhost:5432`  
Banco de dados relacional para integração com Spark e Airflow.  

**Airflow Webserver**  
[http://localhost:8082](http://localhost:8082)  
Interface web do Airflow para monitorar DAGs.  

**Airflow Scheduler**  
Responsável por agendar e executar as DAGs.  

**Airflow Triggerer**  
Responsável por lidar com sensores e disparos assíncronos.  

