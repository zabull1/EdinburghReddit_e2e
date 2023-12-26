import praw
from praw import Reddit
from prawcore.exceptions import RequestException
import pandas as pd
import numpy as np
from utils.constants import POST_FIELDS


# connect to reddit
def connect_to_reddit(client_id: str, secret: str, agent: str) -> Reddit:
    """connect to reddit using api credentials"""

    try:
        reddit = praw.Reddit(
            client_id=client_id, client_secret=secret, user_agent=agent
        )

        print("Reddit connected!!!")

        return reddit

    except RequestException as e:
        # Handle PRAW exceptions related to HTTP requests
        print(f"Error making Reddit API request: {e}")
    except praw.exceptions.PRAWException as e:
        # Handle other PRAW-specific exceptions
        print(f"PRAW Exception: {e}")
    except Exception as e:
        # Handle other unexpected exceptions
        print(f"Unexpected Exception: {e}")


def get_posts(
    reddit: Reddit, subreddit: str, time_filter: str, limit: int
) -> pd.DataFrame:
    """extract posts for a particular subreddit"""

    sub = reddit.subreddit(subreddit)
    posts = sub.top(time_filter=time_filter, limit=limit)

    post_lists = [{key: getattr(post, key) for key in POST_FIELDS} for post in posts]

    return pd.DataFrame(post_lists)


def transform_posts(post_df: pd.DataFrame) -> pd.DataFrame:
    """ transforming the posts dataframe and enforcing each columns datatype"""

    post_df['created_utc'] = pd.to_datetime(post_df['created_utc'], unit='s')
    post_df['over_18'] = np.where((post_df['over_18'] == True), True, False)
    post_df['author'] = post_df['author'].astype(str)
    edited_mode = post_df['edited'].mode()
    post_df['edited'] = np.where(post_df['edited'].isin([True, False]), post_df['edited'], edited_mode).astype(bool)
    post_df['num_comments'] = post_df['num_comments'].astype(int)
    post_df['score'] = post_df['score'].astype(int)
    post_df['title'] = post_df['title'].astype(str)

    return post_df

def load_posts_to_parquet(data: pd.DataFrame, path: str) -> None:
    data.to_parquet(path, index=False)