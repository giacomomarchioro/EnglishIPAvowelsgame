# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 19:36:33 2015
Python IPA Game try to guess what are these vowels

@author: giacomo
"""
import pygame
import os
import sys
import random

soundpath = os.path.abspath(os.path.dirname(sys.argv[0]))+'/Sounds/'
gg ='Close_front_unrounded_vowel'

count=0

soundperround=4
sounds={'Close_front_unrounded_vowel':'i',
'Close_front_rounded_vowel':'y',
'Near-close_near-back_rounded_vowel':'ʊ',
'Near-close_near-back_rounded_vowel':'ʏ',
'Close-mid_front_unrounded_vowel':'e',
'Open-mid_front_unrounded_vowel':'ɛ',
'Near-open_front_unrounded_vowel':'æ',
'Mid-central_vowel':'ə'}

pygame.init()
pygame.mixer.init()

while count<soundperround:
    sound=random.choice(sounds.keys())
    pygame.mixer.music.load(soundpath+sound+'.ogg')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy(): 
        pygame.time.Clock().tick(10)
    answer=raw_input('Use the keybord and type the answer:')
    if answer==sounds[sound]:
        print "Correct! It's a "+sound.replace("_"," ").lower()
    else:
        print "Wrong! It's a "+sound.replace("_"," ").lower()+":"+sounds[sound]
    count+=1
    

    

