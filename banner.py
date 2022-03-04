import socket

s = socket.socket()

ip = input('Input IP ')
port = str(input('Enter port '))

try:
    s.connect((ip,int(port)))
    s.settimeout(5)
    print(str(s.recv(1024)).strip('b'))
except:
    print('que')



