import socket
host = '127.0.0.1'
port = 14100
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()
conn,addr=server.accept()
data=conn.recv(1024)
web_name=data.decode('ASCII')
web_link={"google":"www.google.com","facebook":"www.facebook.com","youtube":"www.youtube.com"}
a=web_link[web_name]
conn.sendall(a.encode('ASCII'))
print("Web link send to client...")
server.close()
