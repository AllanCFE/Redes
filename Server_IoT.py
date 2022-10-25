from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',42069))

def testCommand(command):
    param = None
    if command == "SETAR X" or command == "SETAR Y":
        param = int(input(f"Insira o valor desejado para o comando {command}:"))

    elif command == "REINICIAR" or command == "CONFIGURAR":
        print(command)
    else:
        print("Comando inválido")
        
    try:
        clientName = input("Entrar IP do dispositivo (Formato 000.000.000.000): ")
        clientPort = int(input("Entrar Porta do Dispositivo (Apenas números): "))
    except:
        print("IP ou Porta em formato inválido")
    
    try:
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((clientName, clientPort))
        if param:
            command = command + '-' + str(param)
            print(command)
        clientSocket.send(command.encode())
        deviceResponse = clientSocket.recv(1024)
        print(f"Response from device: {deviceResponse.decode()}")
        clientSocket.close()
    except:
        print("Connection error")

while True:
    try:
        command = input("Enter command:")
    
        testCommand(command)
    except KeyboardInterrupt:
        serverSocket.close()
        print("Server stopped")
        break
    