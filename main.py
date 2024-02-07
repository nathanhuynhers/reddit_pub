#imports
import pymovie
import praw
import requests
from PIL import Image, ImageFont, ImageDraw

reddit = praw.Reddit(
    client_id="OXMNc3nojb2TBjyvAgbJ9w",
    client_secret="W9WteXt0PL0H7B0Jj1s8DrmbyVn9Og",
    user_agent="testing script",
)

subreddit = reddit.subreddit("AmItheAsshole")

#load already published reddit posts
def load_published():
    with open('published_submissions.txt', 'rU') as in_file:
        return in_file.read().split('\n')
    
#add current sub to the published file
def write_published(current_sub):
    return #remove this line when done
    with open('published_submissions.txt', 'w') as out_file:
        out_file.write('\n'.join(already_published))
        out_file.write('\n' + current_sub.url)

#generates the reddit post we will make a video out of
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

    title = curr.title
    text = curr.selftext

    i = Image.open("title_template.jpg")
    title_image = ImageDraw.Draw(i)
    myfont = ImageFont.truetype('C:/Users/natha/Desktop/reddit_pub/IBMPlexSans-Regular.ttf', 30)
    title_image.text((60, 100), title, font = myfont, fill=(0, 0, 0))
    i.show()

    print(text)

    print(curr.title)
    
