from airflow import DAG
from airflow.providers.microsoft.mssql.operators.mssql import MsSqlOperator

from datetime import datetime

with DAG(
    dag_id = "testdag",
    schedule_interval="30 6 * * *",
    start_date=datetime(2022, 1, 1),
    catchup=False) as dag:

    # Error because of missing connection - this is how it should be
    first_task = MsSqlOperator(
        task_id="first_task",
        sql="testdag/testscript.sql")
    
    # Error because of template not found
    second_task = MsSqlOperator(
        task_id="second_task",
        sql="dags/testdag/testscript.sql")

    # When trying to open the file the path has to contain "dags" in the path - why?
    with open("dags/testdag/testscript.sql","r") as file:
        f = file.read()
        file.close()

    first_task
    second_task