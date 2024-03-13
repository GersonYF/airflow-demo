import os
import pandas as pd

data_dir = '/opt/airflow/data'


def load_data():
    csv_file_path = os.path.join(data_dir, 'candidates.csv')
    df = pd.read_csv(csv_file_path, sep=';')

    return df


def save_data(ti):
    df = ti.xcom_pull(task_ids='clean_columns')
    csv_file_path = os.path.join(data_dir, 'anonymized_data.csv')
    df.to_csv(csv_file_path, index=False)
