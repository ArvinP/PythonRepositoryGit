# Step 1: import socket

import socket

# Step 2: Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 3: Get local machine name
host = socket.gethostname()
port = 12345

# Step 4: Bind to the port
server_socket.bind((host, port))

# Step 5: Listen for incoming connections
server_socket.listen(5)

print("Server listening on {}:{}".format(host, port))

while True:
    # Step 6: Establish connection with client
    client_socket, addr = server_socket.accept()
    print('Got connection from', addr)

    # Step 7: Send a thank you message to the client
    client_socket.send(b'Thank you for connecting')

    # Step 8: Close the connection
    client_socket.close()