from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago

import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.main import reddit_pipeline, aws_pipeline

default_args = {"owner": "Aminu Lawal", "start_date": days_ago(1)}

dag = DAG(
    dag_id="Edinburgh_reddit_dag",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
)

file_postfix = datetime.now().strftime("%Y%m%d")
file_name = f"reddit_{file_postfix}"

t = DummyOperator(task_id="Eddinburgh", dag=dag)

extract_posts = PythonOperator(
    task_id="reddit_posts_extraction",
    python_callable=reddit_pipeline,
    op_kwargs={
        "file_name": file_name,
        "subreddit": "Edinburgh",
        "time_filter": "day",
        "limit": 100,
    },
    dag=dag,
)

# load to s3
load_to_s3 = PythonOperator(
    task_id="load_reddit_posts_to_s3", python_callable=aws_pipeline, dag=dag
)

t >> extract_posts >> load_to_s3
