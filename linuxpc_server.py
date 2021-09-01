#### Linux(PC) SERVER #### 

import zmq
import cv2
import base64
import numpy as np

### connect sockets ###
ctx = zmq.Context()
socket = ctx.socket(zmq.REP)
socket.bind("tcp://*:5555")

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

print("before while")
while True:
    try:
       print("waiting for the client to send data")

       img= socket.recv_multipart(4096)
       #print(img)

       #### decode image received from the client ####
       imgdec = base64.b64decode(img[0])
       npimg = np.fromstring(imgdec, dtype=np.uint8)
       source = cv2.imdecode(npimg, 1)

       print("Image decoded")
       ### display received image after decoding ####
       cv2.imshow("image", source)
    
       print("Image received")
       socket.send(b"")

       #print("before decode")
    
       cv2.waitKey(1)
    
    except KeyboardInterrupt:
       cv2.destroyAllWindows()
       print ("\n\nBye bye\n")
       break
    
#print("end of code")
	
