import os
import pandas as pd
from config.config import reddit

def fetch_posts(query="deprem", subreddit="turkey", limit=1500):
    posts = []
    for post in reddit.subreddit(subreddit).search(query, sort="new", limit=limit):
        posts.append([post.title, post.selftext])

    df = pd.DataFrame(posts, columns=["title", "content"])

    # 👇 Klasör yoksa oluştur
    os.makedirs("data", exist_ok=True)

    df.to_csv("data/reddit_posts.csv", index=False)
    return df
