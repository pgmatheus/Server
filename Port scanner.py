import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)
host = input('Enter IP to scan ') # 137.74.187.103
port = int(input('Enter port ')) # 22

def portScanner(port):
    if s.connect_ex((host,port)):
        print('Port is open')
    else:
        print('Port is closed')

portScanner(port)    
