import configparser
import os

parser = configparser.ConfigParser()
path = os.path.join(os.path.dirname("__file__"), "../config/config.conf")
parser.read(path)


# Reddit api
CLIENT_ID = parser.get("reddit_api_keys", "client_id")
SECRET = parser.get("reddit_api_keys", "secret_key")

# aws
AWS_ACCESS_KEY = parser.get("aws", "AWS_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = parser.get("aws", "AWS_SECRET_ACCESS_KEY")
AWS_REGION = parser.get("aws", "AWS_REGION")
BUCKET_NAME = parser.get("aws", "BUCKET_NAME")

# path
# INPUT_PATH = parser.get("file_paths", "input_path")
OUTPUT_PATH = parser.get("file_paths", "output_path")


POST_FIELDS = (
    "id",
    "title",
    "score",
    "num_comments",
    "author",
    "created_utc",
    "url",
    "over_18",
    "edited",
    "spoiler",
    "stickied",
)
