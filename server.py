# TODO: import socket library
from socket import *
import sys
import random
import string
import cv2 


if (len(sys.argv) < 2):
  print("Usage: python3 " + sys.argv[0] + " server_port")
  sys.exit(1)

server_port=int(sys.argv[1])

# TODO: Create a socket for the server on localhost
server = socket(AF_INET, SOCK_STREAM)
# TODO: Bind it to a specific server port supplied on the command line
server.bind(("127.0.0.1", server_port))
# TODO: Put server's socket in LISTEN mode
server.listen(5)
# TODO: Call accept to wait for a connection
(connection, address) = server.accept()
# Repeat NUM_TRANSMISSIONS times
# TODO: receive data over the socket returned by the accept() method
data = connection.recv(4096).decode()
# TODO: print out the received data for debugging
print("Received: " + data)
# TODO: Generate a new string of length 10 using rand_str
randomString = rand_str(10)
# TODO: Append the string to the buffer received
newData = randomString + data
print("Appended: " + newData)
# TODO: Send the new string back to the client
connection.send(newData.encode("utf-8"))
# TODO: Close all sockets that were created
server.close()
connection.close()