import socket
import sys
import random
import cv2 
import pickle
import struct


if (len(sys.argv) < 2):
  print("Usage: python3 " + sys.argv[0] + " receiver_port")
  sys.exit(1)

#receiver port
receiver_port=int(sys.argv[1])

#create a socket
receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind a socket to receiver
receiver.bind(("127.0.0.1", receiver_port))

#listen for connection
receiver.listen(10)

#establish a connection
(connection, address) = receiver.accept()

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
      break
  
  cv2.imshow('frame', pickle.loads(frame_data))

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cv2.destroyAllWindows()
receiver.close()
