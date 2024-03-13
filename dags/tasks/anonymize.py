import hashlib

def anonymize(data):
    return hashlib.md5(data.encode()).hexdigest()


def anonymize_data(ti):
    df = ti.xcom_pull(task_ids='load_data')

    df['First Name'] = [anonymize(name) for name in df['First Name']]
    df['Last Name'] = [anonymize(name) for name in df['Last Name']]
    df['Email'] = [anonymize(email) for email in df['Email']]

    ti.xcom_push(key='anonymized_data', value=df)
