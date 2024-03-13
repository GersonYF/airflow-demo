import os
import pandas as pd

airflow_home = os.getenv('AIRFLOW_HOME', os.path.expanduser('~/airflow'))
data_dir = os.path.join(airflow_home, 'data')


def load_data():
    # Use the data directory path to load the candidates.csv file
    csv_file_path = os.path.join(data_dir, 'candidates.csv')
    df = pd.read_csv(csv_file_path)
    return df

def save_data(ti):
    df = ti.xcom_pull(task_ids='anonymize_data')
    csv_file_path = os.path.join(data_dir, 'anonymized_data.csv')
    df.to_csv(csv_file_path, index=False)
