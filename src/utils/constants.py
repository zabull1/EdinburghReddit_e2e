import configparser
import os

parser = configparser.ConfigParser()
path = os.path.join(os.path.dirname(__file__), '../config/config.conf')
parser.read(path)



CLIENT_ID = parser.get('reddit_api_keys', 'client_id')
SECRET = parser.get('reddit_api_keys', 'secret_key')



POST_FIELDS = (
    'id',
    'title',
    'score',
    'num_comments',
    'author',
    'created_utc',
    'url',
    'over_18',
    'edited',
    'spoiler',
    'stickied'
)