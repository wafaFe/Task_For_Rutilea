#### Raspberry pi CLIENT #### 

import zmq
import cv2
import base64
from base64 import b64encode, b64decode

#connect sockets
ctx = zmq.Context()
socket = ctx.socket(zmq.REQ)
socket.connect("tcp://192.168.1.31:5555")

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
### init the camera in raspberry pi ###
#camera = cv2.VideoCapture(0)  

### reading image from source file ###
image = cv2.imread("assets/wafa.jpg", cv2.IMREAD_COLOR)
while True:
    try:
       ### take picture from camera ###
       #image = camera.shot()
       #(grabbed, frame) = camera.read()

       frame = cv2.resize(image, (640, 480))  # resize the frame
       print("Reading image")
       encoded, buffer = cv2.imencode('.jpg', frame)

       print("Encoding buffer")
       j=base64.b64encode(buffer)    
       #print(j)

       socket.send_multipart([j]) 
       print("Image encoded sent to SERVER")
       message = socket.recv()
       cv2.waitKey(1)
    except KeyboardInterrupt:
       cv2.destroyAllWindows()
       print ("\n\nBye bye\n")
       break

