import nmap

scanner = nmap.PortScanner()
print('welcome')
print('<---------->')

ip_addr = input('Enter IP to scan')
type(ip_addr)
resp = input("""/n Enter Type of scan
                1) SYN
                2) UDP
                3) Comprehensive""")
type(resp)

if resp=='1':
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print(scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print(scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print(scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print(scanner[ip_addr]['udp'].keys())       
elif resp == '3':
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print(scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print(scanner[ip_addr]['tcp'].keys())    
else:
    print('que')