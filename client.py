import sys
import os
import random
import string
import cv2
from socket import *
import numpy as np 
import pickle
import struct

if (len(sys.argv) < 3):
  print("Usage: python "  + sys.argv[0] + " server_port" + "video_file")
  sys.exit(1)

server_port = int(sys.argv[1])
video_file = cv2.VideoCapture(sys.argv[2])

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.connect(('127.0.0.1', server_port))

while video_file.isOpened():
    ret, frame = cap.read()
    payload = pickle.dumps(frame)
    header = struct.pack("H", len(payload))
    tcp_socket.sendall(header + payload)

"""
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

  sock.send(frame)

  if cv2.waitKey(24) & 0xFF == ord('q'):
    break

video.release()


cv2.destroyAllWindows()

print(sys.getsizeof(listOfFrames))

sock.close()
"""
