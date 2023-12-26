import sys
import os
import pandas as pd

# sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.constants import CLIENT_ID, SECRET
from src.etl.edinburghReddit_etl import connect_to_reddit,  get_posts


def reddit_pipeline(subreddit: str, time_filter:str, limit: int | None) -> None:
    """ """
    # connecting to reddit instance
    instance = connect_to_reddit(CLIENT_ID, SECRET, 'Aminu')
    
    # extraction
    posts = get_posts(instance, subreddit, time_filter, limit)




    # print(posts.head(10))

    # return None

