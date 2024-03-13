FROM apache/airflow:2.8.3
RUN pip install --no-cache-dir pandas numpy seaborn matplotlib
