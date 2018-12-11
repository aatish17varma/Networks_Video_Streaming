import sys
import os
import random
import string
import cv2
import socket
import numpy as np 
import pickle
import struct


if (len(sys.argv) < 2):
  print("Usage: python "  + sys.argv[0] + " server_port")
  sys.exit(1)

server_port=int(sys.argv[1])

# 'IMG_4304.mov'

#name of the video you want to display
video = cv2.VideoCapture(sys.argv[2])

#create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect socket to port
sock.connect(('127.0.0.1', server_port))


while True:
  ret, frame = video.read()
  if ret:
      data = pickle.dumps(frame)

      sock.sendall(struct.pack("L", len(data))+data) 

      if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  else:
      break

video.release()
sock.close()
