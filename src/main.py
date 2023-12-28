import os
import pandas as pd
import logging


from src.etl.edinburgh_reddit_etl import (
    connect_to_reddit,
    get_posts,
    transform_posts,
    save_posts_to_parquet,
)

from src.etl.edinburgh_aws_etl import (
    connect_s3,
    check_and_create_bucket,
    load_to_s3_bucket,
)

from src.utils.constants import CLIENT_ID, SECRET, BUCKET_NAME, OUTPUT_PATH, AWS_REGION


def reddit_pipeline(
    file_name: str,
    subreddit: str = "Edinburgh",
    time_filter: str = "day",
    limit: int = None,
) -> None:
    """reddit pipeline"""
    # connecting to reddit instance
    reddit_instance = connect_to_reddit(CLIENT_ID, SECRET)

    # extraction
    posts = get_posts(reddit_instance, subreddit, time_filter, limit)

    # transformation
    posts = transform_posts(posts)
    logging.info(posts.head(10))

    # load to s3
    # path = os.path.join(os.path.dirname("__file__"), f"..{OUTPUT_PATH}") #local directory
    path = OUTPUT_PATH
    file_path = f"{path}/{file_name}.parquet"
    save_posts_to_parquet(posts, file_path)
    return file_path


def aws_pipeline(ti) -> None:
    """aws pipeline"""

    # connect to s3
    s3 = connect_s3()

    check_and_create_bucket(s3, BUCKET_NAME, AWS_REGION)

    path = ti.xcom_pull(task_ids="reddit_posts_extraction", key="return_value")
    print(path)
    s3_file_name = path.split("/")[-1]

    load_to_s3_bucket(s3, path, BUCKET_NAME, s3_file_name)
