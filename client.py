import sys
import os
import random
import string
import cv2
from socket import *
import numpy as np 



# videopath = '~/Desktop/IMG_4304.mov'

if (len(sys.argv) < 2):
  print("Usage: python "  + sys.argv[0] + " server_port")
  sys.exit(1)

video = cv2.VideoCapture('IMG_4304.mov')

print(video.isOpened())

server_port=int(sys.argv[1])

sock = socket(AF_INET, SOCK_STREAM)

sock.connect(('127.0.0.1', server_port))

fps = video.get(cv2.CAP_PROP_FPS)

listOfFrames = []

print('FPS ', fps)

while(video.isOpened()):

  ret, frame = video.read()

  # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  
  # cv2.imshow('frame',gray)
  #   
  cv2.imshow('frame', frame)

  listOfFrames.append(frame)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

video.release()

cv2.destroyAllWindows()

print(sys.getsizeof(listOfFrames))

sock.close()
