from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from tasks import load_data, anonymize_data, clean_columns, save_data


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'db_preparation',
    default_args=default_args,
    description='Anonymize and clear columns attributes of the dataset',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 3, 13),
    catchup=False,
)

t1 = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=dag,
)

t2 = PythonOperator(
    task_id='anonymize_data',
    python_callable=anonymize_data,
    dag=dag,
)

t3 = PythonOperator(
    task_id='clean_columns',
    python_callable=clean_columns,
    dag=dag,
)

t4 = PythonOperator(
    task_id='save_data',
    python_callable=save_data,
    dag=dag,
)

t1 >> t2 >> t3 >> t4
