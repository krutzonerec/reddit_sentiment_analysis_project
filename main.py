import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from src.reddit_scraper import fetch_posts
from src.sentiment_analyzer import analyze_sentiment
from src.visualizer import plot_sentiment_distribution

def main():
    df = fetch_posts()
    df["sentiment"] = df["title"].apply(analyze_sentiment)
    plot_sentiment_distribution(df)

if __name__ == "__main__":
    main()
