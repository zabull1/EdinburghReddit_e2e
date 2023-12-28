import configparser
import os, sys

parser = configparser.ConfigParser()

parser.read(os.path.join(os.path.dirname(__file__), "../../config/config.conf"))

# CONFIG_FILE_PATH = r"/opt/airflow/config/config.conf"
# parser.read(CONFIG_FILE_PATH)

try:
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

except configparser.NoOptionError:
    print("could not read configuration file")
    sys.exit(1)


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
