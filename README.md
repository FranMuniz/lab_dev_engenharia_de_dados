## Laboratório de Desenvolvimento - Engenharia de Dados

Um laboratório completo para estudos em **Engenharia de Dados**, rodando via **Docker**.  
Aqui você encontra um ambiente integrado com **Spark, PySpark, Jupyter, PostgreSQL e Airflow**, pronto para treinar desde consultas SQL até orquestração de pipelines de dados.

---

### 🚀 Tecnologias

- **Apache Spark** → processamento distribuído de dados.
- **PySpark** → API Python para manipulação de dados no Spark.
- **Jupyter Notebook** → ambiente interativo para experimentos.
- **PostgreSQL** → banco de dados relacional para integração com Spark e Airflow.
- **Apache Airflow** → orquestrador de workflows e pipelines de dados.

<p align="center">
  <img src="https://img.shields.io/badge/Spark-FF6F00?style=for-the-badge&logo=apachespark&logoColor=white"/>
  <img src="https://img.shields.io/badge/Spark_SQL-FF6F00?style=for-the-badge&logo=apachespark&logoColor=white"/>
  <img src="https://img.shields.io/badge/Postgres-316192?style=for-the-badge&logo=postgresql&logoColor=white"/>
  <img src="https://img.shields.io/badge/Airflow-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white"/>
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white"/>
  <img src="https://img.shields.io/badge/PySpark-EE4C2C?style=for-the-badge&logo=python&logoColor=white"/>
</p>

---

### 📌 Roadmap de Estudos

- [ ] Fundamentos de Spark (RDD, DataFrames, Lazy Evaluation)  
- [ ] Operações básicas (`select`, `filter`, `groupBy`, `join`)  
- [ ] Leitura e escrita de dados (CSV, Parquet, PostgreSQL)  
- [ ] Spark SQL  
- [ ] Integração Spark + Airflow  
- [ ] Pipelines completos de Engenharia de Dados  

---

## 📂 Estrutura de Pastas

```bash
lab_dev_engenharia_de_dados/
│── docker-compose.yml   # definição dos serviços
│── notebooks/           # Jupyter Notebooks com seus estudos em PySpark
│── dags/                # DAGs do Airflow
│── logs/                # logs do Airflow
│── plugins/             # plugins do Airflow

---

## ⚙️ Como rodar o ambiente

### 1️⃣ Clone este repositório
Clone o repositório e entre na pasta do projeto:  
**Comandos:**  
git clone https://github.com/seu-usuario/meu-lab-dados.git  
cd lab_dev_engenharia_de_dados/

---

### 2️⃣ Suba os serviços com Docker Compose
**Comando:**  
docker-compose up -d

---

### 3️⃣ Acesse os serviços

**🔥 Spark Master**  
[http://localhost:8080](http://localhost:8080)  
Interface web do Spark para acompanhar workers e jobs.

**📒 Jupyter Notebook**  
[http://localhost:8888](http://localhost:8888)  
Ambiente interativo com PySpark já configurado.  
Para ver o token de acesso:  
docker logs jupyter

**🐘 PostgreSQL**  
Host: `localhost:5432`  
Banco de dados relacional para integração com Spark e Airflow.  
- **Usuário:** admin  
- **Senha:** admin  
- **Banco:** mydb
