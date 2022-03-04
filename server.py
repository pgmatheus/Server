from email import message
from http import client
import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
host = '192.168.56.1'

port = 8080

serversocket.bind((host,port))
serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept()
    print("received connection from " + host)

    message = 'thank you for connecting to server' + '\r\n'
    clientsocket.send(message.encode('ascii'))

    clientsocket.close() 
