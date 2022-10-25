from socket import *

deviceSocket = socket(AF_INET, SOCK_STREAM)
devicePort = 25565

deviceSocket.bind(('',devicePort))
deviceSocket.listen(1)

serverAdress = ''
timeX = 0
timeY = 0

def receberComando():
    print("Avacate")
    connectionSocket, addr = deviceSocket.accept()
    message = connectionSocket.recv(1024).decode()
    
    if message == "CONFIGURAR":
        serverAdress = addr
        print(f"SERVIDOR: + {addr}")
        connectionSocket.send("Connected".encode())
        connectionSocket.close()
    elif message == "REINICIAR":
        print(message)
    elif message == "SETAR X":
        print(message)
    elif message == "SETAR Y":
        print(message)
    else:
        print(f"Not recognized: {message}")

while True:
    receberComando()

print(serverAdress)
deviceSocket.close()