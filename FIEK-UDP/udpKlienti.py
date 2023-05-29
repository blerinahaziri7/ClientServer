import socket
UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 14000
#Message = "Hello, Server".encode()

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#clientSock.bind((UDP_IP_ADDRESS,UDP_PORT_NO))
while True:
    msg = input("Operacioni (IP, NRPORTIT, NUMERO, ANASJELLTAS, PALINDROM, KOHA, LOJA, GCF, KONVERTO, MORS,ROMAK)?: ")
    msg=str(msg)
    msg = msg.encode()

    clientSock.sendto(msg, (UDP_IP_ADDRESS, UDP_PORT_NO))
    
    data, addr =clientSock.recvfrom(128)
    print ("Përgjigjja: " + data.decode())
clientSock.close()