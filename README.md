## 💻 Laboratório de Desenvolvimento - Engenharia de Dados

Um laboratório completo para estudos em **Engenharia de Dados**, rodando via **Docker**.  
Aqui você encontra um ambiente integrado com **Spark, PySpark, Jupyter, PostgreSQL e Airflow**, pronto para treinar desde consultas SQL até orquestração de pipelines de dados.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/Spark-FF6F00?style=for-the-badge&logo=apachespark&logoColor=white"/>
  <img src="https://img.shields.io/badge/PySpark-EE4C2C?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Spark_SQL-FF6F00?style=for-the-badge&logo=apachespark&logoColor=white"/>
  <img src="https://img.shields.io/badge/Postgres-316192?style=for-the-badge&logo=postgresql&logoColor=white"/>
  <img src="https://img.shields.io/badge/Airflow-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white"/>
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white"/>
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
</p>

---

### 📂 Estrutura de Pastas

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

---

### Bônus: Roadmap de Estudos

#### Fundamentos de Python
- [ ] Sintaxe básica, variáveis, tipos de dados  
- [ ] Estruturas de controle (`if`, `for`, `while`)  
- [ ] Funções, módulos e pacotes  
- [ ] Listas, dicionários, tuplas e sets  
- [ ] Manipulação de arquivos (CSV, JSON, TXT)  
- [ ] Bibliotecas: `pandas`, `numpy`, `datetime`  

#### Banco de Dados e SQL
- [ ] Conceitos de banco de dados relacional vs não-relacional  
- [ ] Criação de tabelas e inserção de dados  
- [ ] Consultas básicas (`SELECT`, `WHERE`, `ORDER BY`, `GROUP BY`)  
- [ ] Joins (`INNER`, `LEFT`, `RIGHT`, `FULL`)  
- [ ] Funções agregadas e de janela (`SUM`, `COUNT`, `ROW_NUMBER`)  
- [ ] Subqueries e CTEs (`WITH`)  
- [ ] Indexes, constraints e normalização  
- [ ] Prática em PostgreSQL  

#### Git & GitHub
- [ ] Git: clone, add, commit, push, pull  
- [ ] Branches e merges  
- [ ] Pull Requests e code review  
- [ ] GitHub: repositórios, issues, GitHub Actions (CI/CD básico)  

#### Manipulação de Dados com Python
- [ ] Leitura/escrita de dados: CSV, Excel, Parquet  
- [ ] Limpeza de dados: `fillna`, `dropna`, duplicados  
- [ ] Transformações: `apply`, `map`, `merge`, `concat`  
- [ ] Agregações e pivot tables  
- [ ] Validação e qualidade de dados  

#### Apache Spark & PySpark
- [ ] Fundamentos de Spark (RDD, DataFrames, Lazy Evaluation)  
- [ ] Operações básicas (`select`, `filter`, `groupBy`, `join`)  
- [ ] Leitura e escrita de dados (CSV, Parquet, PostgreSQL, S3)  
- [ ] Transformações avançadas (`window functions`, `pivot`, `explode`)  
- [ ] Spark SQL  
- [ ] Otimização: caching, partitioning, broadcast join  
- [ ] PySpark UDFs e UDAFs  

#### Orquestração de Pipelines (Airflow)
- [ ] DAGs e scheduling  
- [ ] Operadores: PythonOperator, BashOperator, PostgresOperator  
- [ ] Variáveis, XCom e templates Jinja  
- [ ] SubDAGs e modularização  
- [ ] Monitoramento de pipelines e alertas  
- [ ] Integração Airflow + Spark + Banco de Dados  

#### Engenharia de Dados na Prática
- [ ] Pipelines de ingestão e transformação  
- [ ] Integração com APIs e sistemas externos  
- [ ] Processamento batch vs streaming  
- [ ] Armazenamento: bancos de dados, data lakes, warehouses  
- [ ] Logging, rastreabilidade e testes de dados  

#### Boas Práticas & Soft Skills
- [ ] Estrutura de pastas e organização de código  
- [ ] Variáveis de ambiente (`.env`)  
- [ ] Controle de dependências (`requirements.txt`, `pipenv`, `poetry`)  
- [ ] Documentação clara e README amigável  
- [ ] Comunicação com time e stakeholders  

#### Extras e Diferenciais
- [ ] Docker para ambientes isolados  
- [ ] CI/CD aplicado a pipelines de dados  
- [ ] Visualização de dados: Matplotlib, Seaborn, Plotly  
- [ ] Conceitos de Big Data: Kafka, Hive, Hudi, Delta Lake  
- [ ] Aprendizado contínuo: cursos, documentação e projetos práticos  


