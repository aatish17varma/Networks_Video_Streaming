import sys
import cv2
from socket import *
import pickle
import struct


if (len(sys.argv) < 3):
    print("Usage: python3 " + sys.argv[0] + " port_number video_file")
    sys.exit(1)

port = int(sys.argv[1])
video_file = sys.argv[2]

# Socket boilerplate
sender = socket(AF_INET, SOCK_STREAM)
sender.connect(('127.0.0.1', port))

# Initialize VideoCapture object for parsing input video frame by frame
video_capture = cv2.VideoCapture(video_file)

while True:
    (isFrame, frame) = video_capture.read()

    if isFrame:
        # Convert frame to byte stream and create header with length of stream
        byte_stream = pickle.dumps(frame)
        header = struct.pack("L", len(byte_stream))

        # Send the frame byte stream
        sender.sendall(header + byte_stream) 
    else:
        break

video_capture.release()
sender.close()
