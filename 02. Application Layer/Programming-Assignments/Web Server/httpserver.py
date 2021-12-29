"""
 Implements a simple HTTP/1.0 Server

"""

import socket


def getIndexPage(page_name):
    file = open(f'htdocs{page_name}')
    content = file.read()
    file.close()
    return content


# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)

while True:
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the client request
    request = client_connection.recv(1024).decode()

    # Parse the client request
    headers = request.split('\n')
    fileName = headers[0].split()[1]
    if fileName == '/':
        fileName = '/index.html'
    
    if fileName == '/favicon.ico': continue

    print(request)

    # Send HTTP response
    response = 'HTTP/1.0 200 OK\n\n' + getIndexPage(fileName)
    client_connection.sendall(response.encode())
    client_connection.close()

# Close socket
server_socket.close()



