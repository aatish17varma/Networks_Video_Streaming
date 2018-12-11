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

video = cv2.VideoCapture('IMG_4304.mov')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', server_port))

# fps = video.get(cv2.CAP_PROP_FPS)

# listOfFrames = []

# print('FPS ', fps)

while True:
  ret, frame = video.read()
  data = pickle.dumps(frame)
  sock.sendall(struct.pack("L", len(data))+data) 

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# video.release()

# cv2.destroyAllWindows()

# print(sys.getsizeof(listOfFrames))

# sock.send(video)
#cv2.imshow('frame', frame)

#   listOfFrames.append(frame)

# sock.close()
