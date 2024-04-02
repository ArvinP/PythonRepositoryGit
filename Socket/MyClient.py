# Step 1: import socket
import socket

# Step 2: Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 3: Get local machine name
host = socket.gethostname()
port = 12345

# Step 4: Connect to server
client_socket.connect((host, port))

# Step 5: Receive data from the server
received_data = client_socket.recv(1024)
# Step 6 : decode the received data
print("Received:", received_data.decode())

# Step 7: Close the connection
client_socket.close()