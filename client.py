# Import socket module
import socket  
import time             

# Create a socket object
s = socket.socket()         

timer1 = 10.0
bw = str(10)
timer = str(timer1)
# Define the port on which you want to connect
port = 12345                

# connect to the server on local computer
s.connect(('127.0.0.1', port))

# receive data from the server
s.send(bw + ' ' + timer)
start = time.time()
received = s.recv(6000)
elapsed = (time.time() - start)
if elapsed <= timer1:
   print received, ' ',str(elapsed)
else:
   print 'time out'
# close the connection
s.close()      
