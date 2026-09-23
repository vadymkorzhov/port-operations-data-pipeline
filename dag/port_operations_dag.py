from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="port_operations_pipeline",
    schedule="@daily",
    start_date=datetime(2019, 1, 1),
    catchup=False,
) as dag:

    ingestion = BashOperator(
        task_id="ingestion",
        bash_command="cd /opt/airflow/ingestion && python pipeline.py"
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="cd /opt/airflow/dbt && dbt run"
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command="cd /opt/airflow/dbt && dbt test"
    )

    ingestion >> dbt_run >> dbt_test