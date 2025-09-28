# dags/pipeline_alphavantage.py
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

# Adiciona projeto_final ao sys.path
PROJECT_PATH = os.path.join(os.path.dirname(__file__), '..', 'projeto_final')
sys.path.append(PROJECT_PATH)

from main import run_pipeline 

default_args = {
    "owner": "Francieli Muniz",
    "depends_on_past": False,
    "start_date": datetime(2025, 9, 21),
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

dag = DAG(
    "pipeline_alphavantage",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False
)

run_task = PythonOperator(
    task_id="executar_pipeline",
    python_callable=run_pipeline,
    dag=dag
)