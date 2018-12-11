# TODO: import socket library
import socket
import sys
import random
import string
import cv2 
import pickle
import struct


if (len(sys.argv) < 2):
  print("Usage: python3 " + sys.argv[0] + " server_port")
  sys.exit(1)

server_port=int(sys.argv[1])

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", server_port))

server.listen(10)

(connection, address) = server.accept()

data = b''

data_size = struct.calcsize("L")

while True:
  while len(data) < data_size:
    data += connection.recv(4096)
  packed_msg_size = data[:data_size]
  data = data[data_size:]
  msg_size = struct.unpack("L", packed_msg_size)[0]
  while len(data) < msg_size:
      data += connection.recv(4096)
  frame_data = data[:msg_size]
  data = data[msg_size:]
  

  frame=pickle.loads(frame_data)
  print(frame)
  cv2.imshow('frame',frame)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break


  # print(sys.getsizeof(data))

  # frame = pickle.loads(data)

  # cv2.imshow('frame', frame)


# server.close()

# connection.close()