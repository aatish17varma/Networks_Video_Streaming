import socket
from socket import error as SocketError
import errno
import sys
import random
import string
import cv2 
import pickle
import struct


if (len(sys.argv) < 2):
  print("Usage: python3 " + sys.argv[0] + " server_port")
  sys.exit(1)

#server port
server_port=int(sys.argv[1])

#create a socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind a socket to server
server.bind(("127.0.0.1", server_port))

#listen for connection
server.listen(10)

#establish a connection
(connection, address) = server.accept()

#emptty byte data used to load frames in
data = b''

data_size = struct.calcsize("L")

while True:
  #while the data we have extracted is less than the data received (struct)
  while len(data) < data_size:
    data += connection.recv(4096)

  packed_msg_size = data[:data_size]
  data = data[data_size:]
  msg_size = struct.unpack("L", packed_msg_size)[0]

  while len(data) < msg_size:
      data += connection.recv(4096)
  
  frame_data = data[:msg_size]
  data = data[msg_size:]
  if not data:
      print("DONE")
      break
  
  cv2.imshow('frame', pickle.loads(frame_data))

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cv2.destroyAllWindows()
server.close()
