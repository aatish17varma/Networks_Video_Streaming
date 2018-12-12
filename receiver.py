import sys
import cv2 
from socket import *
import pickle
import struct

if (len(sys.argv) < 2):
    print("Usage: python3 " + sys.argv[0] + " port_number")
    sys.exit(1)

port = int(sys.argv[1])

# Socket boilerplate
port_socket = socket(AF_INET, SOCK_STREAM)
port_socket.bind(("127.0.0.1", port))
port_socket.listen(10)
(receiver, sender_address) = port_socket.accept()

# Initialize empty bytes object for parsing byte stream
bytes_buffer = b''

# For the purposes of retrieving the header
header_length = struct.calcsize("L")

frames = []

while True:
    while len(bytes_buffer) < header_length:
        bytes_buffer += receiver.recv(4096)

    header = bytes_buffer[:header_length]
    bytes_buffer = bytes_buffer[header_length:]

    frame_size = struct.unpack("L", header)[0]

    while len(bytes_buffer) < frame_size:
        bytes_buffer += receiver.recv(4096)

    frame_data = bytes_buffer[:frame_size]
    bytes_buffer = bytes_buffer[frame_size:]

    frames += [pickle.loads(frame_data)]

    if not bytes_buffer:
        break

port_socket.close()

for frame in frames:
    cv2.imshow('frame', frame)
    cv2.waitKey(33)

cv2.destroyAllWindows()
