from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'Aminu Lawal',
    'start_date': days_ago(1)
}

dag = DAG(
    dag_id = 'test_dag',
    default_args = default_args,
    schedule_interval= '@daily',
    catchup= False
)

test = DummyOperator(
    task_id = 'test_task',

)

test