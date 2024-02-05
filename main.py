#imports
import pymovie
import praw
import requests

reddit = praw.Reddit(
    client_id="OXMNc3nojb2TBjyvAgbJ9w",
    client_secret="W9WteXt0PL0H7B0Jj1s8DrmbyVn9Og",
    user_agent="testing script",
)

subreddit = reddit.subreddit("AmItheAsshole")


if __name__ == "__main__":
 
    for submission in subreddit.hot(limit=3):
        text = submission.selftext
    
    print(text)
    print(type(text))
