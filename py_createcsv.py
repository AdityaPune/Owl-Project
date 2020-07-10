# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 12:41:48 2020

@author: adity
"""

import csv
import os

FOLDER_PATH= r'C:\\Users\\adity\\Desktop\\Owl-Project\\Audio'

def listDir(dir):
  fileNames = os.listdir(dir)
  i=0
  with open('audio_data.csv','w',newline='') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(['Index','fname','label'])
    for fileName in fileNames:
      AUDIO_PATH = dir+'\\'+fileName
      Audios = os.listdir(AUDIO_PATH)
      for Audio in Audios:
        thewriter.writerow([i,Audio,fileName])
        i+=1
    

listDir(FOLDER_PATH)
#with open('audio_data.csv','w',newline='')