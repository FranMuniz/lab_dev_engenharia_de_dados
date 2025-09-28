from sqlalchemy import create_engine, text

DB_USER = "admin"
DB_PASSWORD = "admin"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "lab_dev"

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version();"))
        version = result.fetchone()
        print(f"Conexão bem-sucedida! Versão do PostgreSQL: {version[0]}")

        result_users = conn.execute(text("SELECT id, username, email FROM airflow.ab_user LIMIT 5;"))
        users = result_users.fetchall()
        print("\nUsuários do Airflow (amostra):")
        for user in users:
            print(user)

except Exception as e:
    print(f"Erro ao conectar ou consultar o PostgreSQL: {e}")



