import socket

ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #krijimi i socket
host = '127.0.0.1' #inicizlizimi i ip adreses
port = 14000 #porti

print('Duke pritur lidhjen me serverin perkates')
try:
    ClientSocket.connect((host, port)) #konktimi me server
except socket.error as e:
    print("Nuk kemi konektim me portin dhe serverin e dhene: "+ str(e))

res = ClientSocket.recv(128)
while True:
    
    Input = input('Operacioni (IP, NRPORTIT, NUMERO, ANASJELLTAS, PALINDROM, KOHA, LOJA, GCF, KONVERTO, MORS, ROMAK)?: ')#inputi
    if not Input:
     Input = input('Nuk keni shkruajtur ndonjë kërkesë. Ju lutem kërkesa: ')
       
    ClientSocket.send(str.encode(Input)) #dergimi i kerkeses
    res = ClientSocket.recv(128) #pranimi
    print('Përgjigjja: '+ res.decode('utf-8')) #shtypja

ClientSocket.close() #mbyllja e soketit