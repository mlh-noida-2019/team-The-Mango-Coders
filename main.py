
import vlc
import numpy as np
# Import 
import paralleldots 
# Setting your API key
paralleldots.set_api_key('8l5CH8SRFXhvmYOHsIi6HzpHcaHL5JZq7bD4wKTWVBM')
# Get your API key here
# Viewing your API key 
paralleldots.get_api_key()
# Examples 

# For image path
#path = "/home/my_computer/Downloads/image_1.jpg"
#paralleldots.facial_emotion( path )

#//For image url
url = "http://i.imgur.com/klb812s.jpg"
a =paralleldots.facial_emotion_url( url )
express = a['facial_emotion'][0]['tag']

e = {'Angry':0,'Suprise':1,'Sad':2,'Neutral':3,'Happy':4,'Fear':5,'Disgust':6}

s = {0:['a0','a1'],1:['s0','s1'],2:['sa0','sa1'],3:['n0','n1'],4:['h0','h1'],5:['f0','f1'],6:['d0','d1']}

ran = np.floor(np.random.random(1)*2)
if ran == 0.0:
	ran = 0
elif ran == 1.0:
	ran = 1
song = s[e[express]][ran]+'.mp3'
#print(song)
player = vlc.MediaPlayer(song)
#player =
player.play()
input("ctrl+z to exit")
