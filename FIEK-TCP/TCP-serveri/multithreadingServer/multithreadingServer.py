import socket 
import os
from _thread import *
import random
from datetime import date
from datetime import datetime
import math

ServerSideSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #krijimi i socket
host = '127.0.0.1' 
port = 14000 
ThreadCount = 0 
try: 
 ServerSideSocket.bind((host, port)) 
except socket.error as e:
 print(str(e)) 

print('Socket po pret pret kerkesa..')
ServerSideSocket.listen(5)

def multi_threaded_client(connection, addr):
    connection.send(str.encode('Server i:'))
    while True:  
        data = connection.recv(128) 
        data1=str(data.decode('utf-8'))
        d=data1.lower() 
        list=d.split() 
        
        lista2=data1.split()  
        listaA=lista2[1:] 
         #fjalori per kodin mors
        morseCodeDict = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
        #numrat romak
        numratR = {'I': 1,
                   'V': 5,
                   'X': 10,
                   'L': 50,
                   'C': 100,
                   'D': 500,
                   'M': 1000,
                  }
        
        def IP(): 
            p1=str(addr) 
            pergjigjja="IP Adresa e klientit eshte: " +p1[2:11] 
            connection.sendall(str.encode(pergjigjja)) 
        
        def NRPORTIT(): 
            p1=str(addr)    
            pergjigjja="Klienti eshte duke perdorur portin: " +p1[14:19] 
            connection.sendall(str.encode(pergjigjja)) 
        def NUMERO(list): 
            lista2 = list[1 : ] 
            def listToString(s):  
                str1 = " "       
                return (str1.join(s)) 
            
            fjalia=(listToString(lista2)) 
            if not fjalia:  
             pergjigjja="Ju nuk keni dhene tekst" 
            else: 
             f=filter(str.isalpha, fjalia) 
             vowels = 0 
             consonant = 0 
             for i in f: 
                if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'): 
                    vowels=vowels+1 
                else: 
                    consonant=consonant+1 
             pergjigjja="Ky tekst ka "+str(vowels)+" zanore "+str(consonant)+" bashtingellore" 
            
                
            connection.sendall(str.encode(pergjigjja)) 
        def ANASJELLTAS(listaA): 
            
            def listToString(l): 
                str1 = " "  
                return (str1.join(l)) 

            fjaliaK=(listToString(listaA)) 
            if not fjaliaK: 
             pergjigjja="Ju nuk keni dhene tekst" 
            else: 
             def rev_sentence(sentence):  
                words = sentence.split(' ') 
                reverse_sentence = ' '.join(reversed(words)) 
                return reverse_sentence 
             fjalia=rev_sentence(fjaliaK) 

             def reverseWordSentence(Sentence): 
                words = Sentence.split(" ") 
                newWords = [word[::-1] for word in words] 
                newSentence = " ".join(newWords) 
                return newSentence 
             pergjigjja=reverseWordSentence(fjalia) 
            connection.sendall(str.encode(pergjigjja))  
        def PALINDROM(lista): 

            listaP=lista[1:]  
            def listToString(l): 
                str1 = ""   
                return (str1.join(l)) 

            fjaliaP=(listToString(listaP)) 
            if not fjaliaP: 
             pergjigjja="Ju nuk keni dhene tekst" 
            else: 
             def isPalindrome(t1): 
               t1 = t1.lower() 
               l = len(t1) 

               if l < 2: 
                return True
               elif t1[0] == t1[l - 1]: 
                return isPalindrome(t1[1: l - 1]) 
               else: 
                return False 
             ans = isPalindrome(fjaliaP) 
             if ans==True: 
                pergjigjja="Teksti i dhene eshte palindrom" 
             else: 
                pergjigjja="Teksti i dhene nuk eshte palindrom" 
            
            connection.sendall(str.encode(pergjigjja)) 
        def KOHA(): 
            now = datetime.now() 
            current_time = now.strftime('%d/%m/%Y %I:%M:%S %p') 
            pergjigjja =str(current_time) 
            connection.sendall(str.encode(pergjigjja)) 
        def LOJA(num,start,end):  
            arr = [] 
            tmp = random.randint(start, end) 
            for x in range(num): 
                while tmp in arr: 
                    tmp = random.randint(start, end) 
                arr.append(tmp) 
            arr.sort() 
            pergjigjja=str(arr) 
            connection.sendall(str.encode(pergjigjja)) 
        
        def GCF(numri1, numri2): 
           try: 
            n1=int(numri1)
           except ValueError: 
            p1="Keni dhene gabim parametrin 1" 
            connection.sendall(str.encode(p1)) 
            return 
           try: 
             n2=int(numri2)
           except ValueError: 
             p2="Keni dhene gabim paramentrin 2"
             connection.sendall(str.encode(p2)) 
             return 
             
           GCF=math.gcd(n1,n2) 
           pergjigjja=str(GCF) 
           connection.sendall(str.encode(pergjigjja)) 
        def KONVERTO(opcioni,numri): 
            op=opcioni.lower() 
            try: 
             n1=float(numri)
            except ValueError:
             p1="Vlera qe duhet konvertuar duhet te jete numer" 
             connection.sendall(str.encode(p1))
             return
            if(op=='cmneinch'): 
                                
                rezultati = n1/2.54
                pergjigjja=op + " " + str(round(rezultati,2))
                connection.sendall(str.encode(pergjigjja))
            elif(op=='inchnecm'):
                rezultati = n1 * 2.54
                pergjigjja=op + " " + str(round(rezultati,2))
                connection.sendall(str.encode(pergjigjja))
            elif(op=='kmnemiles'):
                rezultati = n1/1.609
                pergjigjja=op + " " + str(round(rezultati,2))
                connection.sendall(str.encode(pergjigjja))
            elif(op=='milenekm'):
                rezultati = n1*1.609
                pergjigjja=op + " " + str(round(rezultati,2))
                connection.sendall(str.encode(pergjigjja))
            else:
                pergjigjja="Kontrolloni metoden sepse diqka nuk eshte ne rregull.Opsionet jane: kmNeInch, inchNeKm, kmNeMiles,mileNeKm"
                pergjigjja=str(pergjigjja)
                connection.sendall(str.encode(pergjigjja))
        def NDRYSHO(poJo,serveri,porti):  
            if(poApoJo=='po'): 
               list=serveri.split() 
               try: 
                n1=list[0]
                n2=list[2]
                n3=list[4]
                n4=list[6]
                n1=int(numri)
                n2=int(numri)
                n3=int(numri)
                n4=int(numri)
               except Exception: 
                 p1="Adrese jovalide"
                 connection.sendall(str.encode(p1))
                 return  
               try: 
                p=int(porti)
               except ValueError: 
                 p1="Adrese jovalide"
                 connection.sendall(str.encode(p1))
                 return
               if(list[1]=='.' and list[3]=='.' and list[5]=='.'): 
                if(n1>=0 and n1<255 and n2>=0 and n2<255 and n3>=0 and n3<255 and n4>=0 and n4<255): 
                 if(p>0 and p<65535): 
                    addr[0]=serveri 
                    addr[1]=porti 
                    pergjigjja="Porti dhe serveri u ndryshuan me sukses" 
                    pergjigjja=str(pergjigjja)
                    connection.sendall(str.encode(pergjigjja))
                 else:
                    pergjigjja="Kontrolloni perseri te dhenat" 
                    pergjigjja=str(pergjigjja)
                    connection.sendall(str.encode(pergjigjja))
                    return
        def MORS(list): 
          cipher = '' 
          lista2 = list[1 : ] 
          def listToString(s):  
             str1 = " "
             return (str1.join(s))
          fjaliav=(listToString(lista2))
          fjalia=fjaliav.upper() 
          if not fjalia: 
            pergjigjja="Ju nuk keni dhene tekst"
            pergjigjja=str(pergjigjja)
            connection.sendall(str.encode(pergjigjja))
            return
          else:
           for letter in fjalia: 
            if letter != ' ': 
            
             cipher += morseCodeDict[letter] + ' '
            else:
            
             cipher += ' ' 
           pergjigjja=cipher
           pergjigjja=str(pergjigjja)
           connection.sendall(str.encode(pergjigjja))
           return
        
        def ROMAK(numri): 
            numri=numri.upper() 
           
            sum = 0 
            for i in range(len(numri) - 1): 
                left = numri[i] 
                right = numri[i + 1] 
                if numratR[left] < numratR[right]: 
                    sum -= numratR[left] 
                else: 
                    sum += numratR[left]  
            sum += numratR[numri[-1]] 
            pergjigjja=sum 
            pergjigjja=str(pergjigjja) 
            connection.sendall(str.encode(pergjigjja)) 

        
        if(list[0]=='koha'):
           KOHA()
        elif(list[0]=='ip'):
            IP()
        elif(list[0]=='nrportit'):
            NRPORTIT()
        elif(list[0]=='numero'):
            NUMERO(list)
        elif(list[0]=='anasjelltas'):
            ANASJELLTAS(listaA)
        elif(list[0]=='palindrom'):
            PALINDROM(list)
        elif(list[0]=='loja'):
            num=5
            start=1
            end=35
            LOJA(num,start,end)
        elif(list[0]=='gcf'):
         if(len(list)==3):
          n1=list[1]
          n2=list[2]
          GCF(n1,n2)
         elif(len(list)>3):
            pergjigjja="Ka me shume parametra se qe duhet"
            connection.sendall(str.encode(pergjigjja))
         elif(len(list)<3):
            pergjigjja="Nuk ka parametra mjaftueshem"
            connection.sendall(str.encode(pergjigjja))

        elif(list[0]=='konverto'):
            if(len(list)==3):
             KONVERTO(list[1],list[2])
            elif(len(list)>3):
             pergjigjja="Keni dhene me shume parametra se qe duhet per te realizuar konvertimin"
             connection.sendall(str.encode(pergjigjja))
            elif(len(list)<3):
             pergjigjja="Duhet te kete me shume parametra qe kjo metode te perktahet"
             connection.sendall(str.encode(pergjigjja))
        elif(list[0]=='ndrysho'):
            if(len(list)==4):
             if(list[1]=='jo'):
              pergjigjja="Nuk kemi ndryshim te portit apo serverit"
              connection.sendall(str.encode(pergjigjja))
              return
             elif(list[1]=='po'):
              poApoJo=list[1]
              serveri=list[2]
              porti=list[3]
              NDRYSHO(poApoJo,serveri,porti)
            elif(len(list)<4):
             pergjigjja="Nuk kemi parametra mjaftueshem"
             connection.sendall(str.encode(pergjigjja))
            elif (len(list)>4):
             pergjigjja="Keni dhene me shume parametra se qe duhet"
             connection.sendall(str.encode(pergjigjja))
        elif(list[0]=='mors'):
            if(len(list)>=2):
             MORS(list)
            elif(len(list)<2):
             pergjigjja="Keni dhene me pak parametra se qe duhet"
             connection.sendall(str.encode(pergjigjja))             
        elif(list[0]=='romak'):
            if (len(list)==2):
             ROMAK(list[1])
            elif(len(list)<2):
             pergjigjja="Keni dhene me pak parametra se qe duhet"
             connection.sendall(str.encode(pergjigjja))
            elif(len(list)>2):
             pergjigjja="Keni dhene me shume parametra se qe duhet"
             connection.sendall(str.encode(pergjigjja))
        else:
            pergjigjja="Kerkesa e dhene duhet te jete gabim "
            connection.sendall(str.encode(pergjigjja))




    connection.close() 


while True:
    Client, address = ServerSideSocket.accept() 
                                                
    print('Connected to: ' + address[0] + ':' + str(address[1])) 
    start_new_thread(multi_threaded_client, (Client, address)) 
                                                               
    ThreadCount += 1 
    print('Thread Number: ' + str(ThreadCount)) 
ServerSideSocket.close()