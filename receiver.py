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

# This will store the frames of the video
frames = []

# Initialize empty bytes object for parsing byte stream, get length of header
bytes_buffer = b''
header_length = struct.calcsize("L")

while True:
    # Use header_length to get just the header to calculate length of stream
    while len(bytes_buffer) < header_length:
        bytes_buffer += receiver.recv(4096)

    header = bytes_buffer[:header_length]
    bytes_buffer = bytes_buffer[header_length:]

    frame_length = struct.unpack("L", header)[0]

    # Using frame_length, receive full frame in byte stream form
    while len(bytes_buffer) < frame_length:
        bytes_buffer += receiver.recv(4096)

    # Get pickled frame byte stream, and prepare buffer for next receive
    frame_data = bytes_buffer[:frame_length]
    bytes_buffer = bytes_buffer[frame_length:]

    # Unpickle the byte stream frame data to get the frame object
    frames += [pickle.loads(frame_data)]

    # If no more frames, end receiving
    if not bytes_buffer:
        break

port_socket.close()

# Play video
for frame in frames:
    cv2.imshow('frame', frame)
    cv2.waitKey(33)

cv2.destroyAllWindows()
