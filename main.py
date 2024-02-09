#imports
import pymovie
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


already_published = load_published()

if __name__ == "__main__":
 
    
    
    submissions = subreddit.top(time_filter="week", limit=20)

    curr = generate_submission(submissions)
    
    write_published(current_sub=curr)

    title = curr.title
    text = curr.selftext

    generate_title_image(title=title)

    # tts = TTS("tts_models/en/ljspeech/speedy-speech")
    # tts.tts_to_file(text=title, output_path="tts_audio_file.wav")
    gtts.tokenizer.symbols.SUB_PAIRS.append(('AITA', 'Am I the Asshole'))
    tts = gTTS(text=text)
    tts.save("tts_audio_file.wav")
    
    # data, samplerate = sf.read('tts_audio_file.wav')
    # # Play back at 1.5X speed
    # y_stretch = pyrb.time_stretch(data, samplerate, 1.5)
    # # Play back two 1.5x tones
    # y_shift = pyrb.pitch_shift(data, samplerate, 1.5)
    # sf.write("1.5 speedup.wav", y_stretch, samplerate, format='wav')


    root = "tts_audio_file.wav"
    velocidad_X = 1.35 # No puede estar por debajo de 1.0

    sound = AudioSegment.from_file(root)
    so = sound.speedup(velocidad_X, 150, 25)
    so.export(root[:-4] + '_Out.wav', format = 'wav')






    
