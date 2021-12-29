from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
while True:
    connectionSocket, clientAddress = serverSocket.accept()
    print(f"Receiving from {clientAddress}")
    modifiedMessage = connectionSocket.recv(1024).decode().upper()
    connectionSocket.send(modifiedMessage.encode())
    connectionSocket.close()
