#imports
import pymovie
from moviepy.editor import *
import praw
import requests
import textwrap
from PIL import Image, ImageFont, ImageDraw
from gtts import gTTS
from gtts.tokenizer import pre_processors
import gtts.tokenizer.symbols
from pydub import AudioSegment
from pydub import effects
import soundfile as sf
import pyrubberband as pyrb
import librosa



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
        if sub.url not in already_published and len(sub.title) < 160:
            return sub
    print("No more stories")

#gets the title template and puts the title text onto the template
def generate_title_image(title):
    i = Image.open("title_template.jpg")
    title_image = ImageDraw.Draw(i)
    fontsize = 25
    print(fontsize)
    myfont = ImageFont.truetype('C:/Users/natha/Desktop/reddit_pub/IBMPlexSans-Regular.ttf', fontsize)
    margin = 20
    offset = 80
    for line in textwrap.wrap(title, width=40):
        title_image.text((margin, offset), line, font=myfont, fill=(0, 0, 0))
        offset += fontsize

    i.save("title_temp_curr.jpg")

def speedupaudio(root, velocity):

    sound = AudioSegment.from_file(root)
    so = sound.speedup(velocity, 150, 25)
    so.export(root[:-4] + '_Out.wav', format = 'wav')

def getduration(root):
    return librosa.get_duration(filename=root)

def combineaudio(a1, a2):
    sound1 = AudioSegment.from_wav(a1)
    sound2 = AudioSegment.from_wav(a2)

    combined = sound1 + sound2
    combined.export("introandstory.wav", format="wav")

def createvideo():
    
    
    introlength = getduration("audiointro_Out.wav")
    storylength = getduration("tts_audio_file_Out.wav")
    combineaudio("audiointro_Out.wav", "tts_audio_file_Out.wav")
    # video = VideoFileClip("BackgroundVid.mp4").set_duration(introlength + storylength)
    video = VideoFileClip("BackgroundVid.mp4").set_duration(20) #testing purposes

    title = ImageClip("title_temp_curr.jpg").set_start(0).set_duration(introlength).set_pos(("center","center")).resize(height=180)
          #.resize(height=50) # if you need to resize...
    audioclip = AudioFileClip("introandstory.wav")
    video = video.set_audio(audioclip)
          

    final = CompositeVideoClip([video, title])
    final.write_videofile("finalvid.mp4")


already_published = load_published()

if __name__ == "__main__":
 
    
    
    submissions = subreddit.top(time_filter="week", limit=20)

    curr = generate_submission(submissions)
    
    write_published(current_sub=curr)

    title = curr.title
    text = curr.selftext

    generate_title_image(title=title)


    gtts.tokenizer.symbols.SUB_PAIRS.append(('AITA', 'Am I the Asshole'))
    tts = gTTS(text=text)
    tts.save("tts_audio_file.wav")    

    tts = gTTS(text=title)
    tts.save("audiointro.wav")

    speedupaudio("tts_audio_file.wav", 1.35)
    speedupaudio("audiointro.wav", 1.35)

    createvideo()

    






    
