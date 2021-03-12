import socket
host = '127.0.0.1'
port = 14100
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((host,port))
print("Connection Established...")
a=input("enter the website name : ")
c.send(a.encode('ASCII'))
web=c.recv(1024) 
print("Website link is : " , web.decode('ASCII'))
c.close()
