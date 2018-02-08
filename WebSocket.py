#import socket module
from socket import *

serverPort = 80 #Port Used
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print "The server is ready to receive"

while True:
    #Establish the connection
    print 'Ready to serve...'
    connectionSocket, addr = serverSocket.accept()   
    
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        print outputdata    
        connectionSocket.send('\nHTTP OK\n')
        connectionSocket.send(outputdata)    
    
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()   

    except IOError:
        connectionSocket.send('\n404 Not Found\n')
        connectionSocket.send('\n404 Not Found\n')
    
