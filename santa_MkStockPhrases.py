#!/bin/python

#record in audacity. Add reverb. separate on silences, multiple export mp3.

import os, sys, random
import datetime
from pydub import AudioSegment
from pydub.playback import play
import numpy as np
import glob


workingdir = "/home/gibby/santa/"
phrases = glob.glob(workingdir+"santaphrases/*")
musics = glob.glob(workingdir+"music/*")

for i in range(0,len(phrases)):
  #load the files
  phrase = AudioSegment.from_mp3(phrases[i])
  music = AudioSegment.from_mp3(musics[i%(len(phrases)-1)])
  #print their info
  print(phrase)
  print(music)
  print(phrase.duration_seconds)
  #fade in music. 
  seconds = 0
  # 1 second fade in music, 4 seconds music (total 5), bring music down and speaking in-bring up last 1.5 seconds, 3 seconds fade out
  music_mix = music[0:1000].fade_in(1000) + music[1000:5000] + music[5000:(phrase.duration_seconds-1.5)*1000+5000].apply_gain(-18) + music[(phrase.duration_seconds-1.5)*1000+5000:(phrase.duration_seconds)*1000+5000] + music[phrase.duration_seconds*1000+5000:phrase.duration_seconds*1000+8000].fade_out(3000)
  #music_mix = music_mix.apply_gain(-22) #little speaker has some trouble with loud stuff
  phrase_mix = AudioSegment.silent(duration=5000) + phrase + AudioSegment.silent(duration=3000)
  #phrase_mix = phrase_mix.apply_gain(-22)
  #now mix
  mix = music_mix.overlay(phrase_mix, position=0)
  mix = mix.set_frame_rate(6000) #reduce filesize
  mix = mix.set_channels(1) 
  #play(mix)
  mix.export(workingdir + "mixedphrases/" + str(i) + ".mp3", format="mp3")
  
