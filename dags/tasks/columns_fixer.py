from typing import List

def clean_column_names(columns) -> List[str]:
    """
    Clean column names by converting them to lower case and replacing spaces and hyphens with underscores.
        :param columns: list of column names
        :return: list of cleaned column names

    """
    return [col.lower().replace(" ", "_").replace("-", "_") for col in columns]


def clean_columns(ti):
    df = ti.xcom_pull(task_ids='anonymize_data')
    df.columns = clean_column_names(df.columns)

    return df
