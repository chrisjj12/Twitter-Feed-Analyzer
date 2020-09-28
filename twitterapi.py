import keys
import tweepy
import test_video
import wget
from PIL import Image, ImageDraw, ImageFont
import os
import io
import time

def choose_username(username):
    auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
    auth.set_access_token(keys.access_token, keys.access_secret)
    api = tweepy.API(auth)

    public_tweets = api.user_timeline(id = username)

    #def pull_tweets(public_tweets):
    media_files = set()
    texts = []
    j = 0
    for status in public_tweets:
        print(status.text)
        texts.append(status.text)
        media = status.entities.get('media', [])

        img = Image.new('RGB', (1000, 500), color = (73, 109, 137))
        d = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 15)
        d.text((10,10), status.text, fill=(255,255,0), font = font)
        tmp_name = 'tweet' + str(j) + '.png'
        img.save(tmp_name)
        j = j + 1
        
        if(len(media) > 0):
            temp = wget.download(media[0]['media_url'])
            tmp_name2 = 'tweet' + str(j) + '.png'
            im1 = Image.open(temp)
            im1.save(tmp_name2)
            j = j + 1
        
    #def make_video(username):
    pid = os.getpid()
    os.system('ffmpeg -framerate 0.5 -i '+'tweet'+'%d.png video'+str(pid)+'.avi')
    return 0


