from sqlalchemy import create_engine, text

DB_USER = "admin"
DB_PASSWORD = "admin"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "lab_dev"

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
    client_encoding='utf8'
)

sql = """
-- Criar schema
CREATE SCHEMA IF NOT EXISTS brbi_lab;

-- Tabela Bronze
CREATE TABLE IF NOT EXISTS brbi_lab.br_alphavantage_s0_daily_raw (
    data_ref DATE NOT NULL,
    open FLOAT NOT NULL,
    high FLOAT NOT NULL,
    low FLOAT NOT NULL,
    close FLOAT NOT NULL,
    volume BIGINT NOT NULL,
    file_name VARCHAR NOT NULL,
    grass_date DATE NOT NULL,
    ingestion_timestamp TIMESTAMP
);

-- Tabela Silver
CREATE TABLE IF NOT EXISTS brbi_lab.br_alphavantage_s0_daily_live (
    data_ref DATE NOT NULL,
    open FLOAT NOT NULL,
    high FLOAT NOT NULL,
    low FLOAT NOT NULL,
    close FLOAT NOT NULL,
    volume BIGINT NOT NULL,
    file_name VARCHAR NOT NULL,
    grass_date DATE NOT NULL,
    ingestion_timestamp TIMESTAMP,
    CONSTRAINT pk_silver PRIMARY KEY (data_ref)
);

-- Tabela Gold 
CREATE TABLE IF NOT EXISTS brbi_lab.br_alphavantage_s0_daily_refined (
    data_ref DATE NOT NULL,
    avg_price FLOAT NOT NULL,       -- exemplo: média diária ((open+high+low+close)/4)
    total_volume BIGINT NOT NULL,
    file_name VARCHAR NOT NULL,
    grass_date DATE NOT NULL,
    ingestion_timestamp TIMESTAMP,
    CONSTRAINT pk_gold PRIMARY KEY (data_ref)
);

-- Tabela de controle de processamento de arquivos
CREATE TABLE IF NOT EXISTS brbi_lab.br_alphavantage_s0_file_log (
    id SERIAL PRIMARY KEY,
    data_ref DATE NOT NULL,
    file_name VARCHAR(255) NOT NULL,
    status VARCHAR(20) NOT NULL, -- 'sucesso' ou 'falha'
    processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

with engine.connect() as conn:
    conn.execute(text(sql))
    conn.commit()

print("Schema e tabelas criadas com sucesso no schema 'brbi_lab'.")
