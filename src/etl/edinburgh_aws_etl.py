import boto3
from botocore.exceptions import ClientError
import logging
from src.utils.constants import AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY, AWS_REGION


def connect_s3() -> boto3.client:
    """connect to aws s3"""

    try:
        s3 = boto3.client(
            "s3",
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_REGION,
        )

        logging.info("connected to s3")
        return s3
    except Exception as e:
        logging.error("Error connecting to s3: %s", e)
    return None


def check_and_create_bucket(
    s3: boto3.client, bucket: str, region: str = AWS_REGION
) -> None:
    """Create an S3 bucket if doesn't exist"""

    # Check if the bucket already exists
    try:
        s3.create_bucket(
            Bucket=bucket,
            CreateBucketConfiguration={"LocationConstraint": region},
        )

        logging.info("Bucket %s created successfully.", bucket)

    except ClientError:
        logging.info("Bucket %s already exists.", bucket)

    except Exception as create_error:
        logging.error("Error creating bucket %s': %s", bucket, create_error)


def load_to_s3_bucket(
    s3: boto3.client, path: str, bucket: str, s3_file_name: str
) -> None:
    """loading posts data to s3 bucket"""
    try:
        s3_key_name = f"raw/{s3_file_name}"
        s3.upload_file(path, bucket, s3_key_name)
        logging.info("Uploaded %s to s3 bucket %s", s3_key_name, bucket)

    except Exception as e:
        logging.error("Error: %s was not found \n%s", s3_key_name, e)
