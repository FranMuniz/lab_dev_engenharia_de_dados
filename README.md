## 💻 Laboratório de Desenvolvimento - Engenharia de Dados

Um laboratório completo para estudos em **Engenharia de Dados**, rodando via **Docker**.  
Aqui você encontra um ambiente integrado com **Spark, PySpark, Jupyter, PostgreSQL, MinIO, Metabase e Airflow**, pronto para treinar desde consultas SQL até orquestração de pipelines de dados, armazenamento S3 local e visualização.
Sinta-se à vontade para utilizar o lab e explorar todos os serviços!


<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white"/>
  <img src="https://img.shields.io/badge/Spark-FF6F00?style=for-the-badge&logo=apachespark&logoColor=white"/>
  <img src="https://img.shields.io/badge/PySpark-EE4C2C?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Spark_SQL-FF6F00?style=for-the-badge&logo=apachespark&logoColor=white"/>
  <img src="https://img.shields.io/badge/MinIO-26A69A?style=for-the-badge&logo=minio&logoColor=white"/>
  <img src="https://img.shields.io/badge/Postgres-316192?style=for-the-badge&logo=postgresql&logoColor=white"/>
  <img src="https://img.shields.io/badge/Airflow-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/Metabase-509EE3?style=for-the-badge&logo=metabase&logoColor=white"/>
</p>

---

### Pré-requisitos

Antes de iniciar, certifique-se de que sua máquina possui:

- **Docker** (recomendado versão 20+): para rodar os containers.
- **Docker Compose** (versão 1.27+ ou integrada no Docker Desktop): para subir todos os serviços do lab com um único comando.
- **Git**: para clonar o repositório.
- **Python 3.9+** (opcional, caso queira gerar a chave Fernet ou testar scripts fora do container).
- **PostgreSQL**: é recomendado criar **schemas separados** para cada serviço (por exemplo, `airflow` e `metabase`) para evitar conflito de tabelas internas.

Exemplo de criação de schemas:
```sql
-- Schema para Airflow
CREATE SCHEMA IF NOT EXISTS airflow;
GRANT ALL PRIVILEGES ON SCHEMA airflow TO admin;

-- Schema para Metabase
CREATE SCHEMA IF NOT EXISTS metabase;
GRANT ALL PRIVILEGES ON SCHEMA metabase TO admin;
```
> ⚠️ Lembre-se: o lab foi desenvolvido para **localhost**, então todas as portas (8080, 8081, 8082, 8888, 9000, 9090, 3000 e 5432) devem estar livres na sua máquina.

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
Arquivo disponível no repositório, atualize com suas credenciais

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

**MinIO (S3 Local)**  
[http://localhost:9090](http://localhost:9090)  
Console web para gerenciar buckets e arquivos, simulando o S3  

**Metabase**  
[http://localhost:3000](http://localhost:3000)  
Console web para visualização e criação de dashboards com os dados do PostgreSQL  

**Airflow Webserver**  
[http://localhost:8082](http://localhost:8082)  
Interface web do Airflow para monitorar DAGs.  

**PostgreSQL**  
Host: `localhost:5432`  
Banco de dados relacional para integração com Spark e Airflow. 

**Airflow Scheduler**  
Responsável por agendar e executar as DAGs.  

**Airflow Triggerer**  
Responsável por lidar com sensores e disparos assíncronos.  
