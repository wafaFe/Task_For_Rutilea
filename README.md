# Sending camera image from client to server
## About
Programs to send image from a Raspberry pi Client to a server On-premiss(linux PC). 
### My used environment to run this project : <br/>
PC running Linux <br/>
Raspberry pi running debian <br/>
### Prerequisites : <br/>
- Opencv 4.2.0 <br/>
- Python 3.6.9 <br/>
- ZMQ protocol <br/>

In order to run the project (from both server and client) you should use :<br/> 
`python3 <filename.py>` 

To establish a communication with the Raspberry pi you should have an ssh protocol working : <br/>
- You can use the cmdline to tipe : `ssh pi@<PiAddress>` <br/>
- Or via Putty

## Image Output<br/>

- Output from client side <br/>
Sending the chosen image from Raspberry Pi to Server 
<p align="center"><img src="https://github.com/wafaFe/Task_For_Rutilea/blob/main/ImageReadme/Raspi_client_output.png" alt="Client Raspberry pi Output"></p>

After running both programs of the client from the raspberry pi and of the server from linux PC <br/>
The server listens for arrival data from sockets

- When received, the image is displayed from Server side
<p align="center"><img src="https://github.com/wafaFe/Task_For_Rutilea/blob/main/ImageReadme/linux_server_Output.jpg" alt="Server Output"></p>
