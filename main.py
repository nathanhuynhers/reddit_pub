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

def load_published():
    with open('published_submissions.txt', 'rU') as in_file:
        return in_file.read().split('\n')
    
def write_published(current_sub):
    with open('published_submissions.txt', 'w') as out_file:
        out_file.write('\n'.join(already_published))
        out_file.write('\n' + curr.url)

def generate_submission(submissions):
    for sub in submissions:
        if sub.url not in already_published:
            return sub
    print("No more stories")


already_published = load_published()

if __name__ == "__main__":
 
    
    
    submissions = subreddit.top(time_filter="week", limit=20)

    curr = generate_submission(submissions)
    
    write_published(current_sub=curr)

    print(curr.url)

    print(curr.title)
    
