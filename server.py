import socket 
import threading 

host = '127.0.0.1'
port = 555555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Empty lists for the clients and their respective nicknames 
clients = []
nicknames = []

# Sends messages to all clients connected 
def broadcast(message):
  for client in clients:
    client.send(message)
    
def handle(client):
  while True:
    try:
      message = client.recv(1024)
      broadcast(message)
      
    except:
      index = clients.index(client)
      clients.remove(client)
      client.close()
      nickname = nicknames[index]
      broadcast(f'{nickname} left the chat!'.encode('ascii'))
      nicknames.remove(nickname)
      break

def receive():
  while True:
    client, address = server.accept()  # accepting the connection 
    print(f'Connected with {str(address)}')
    
    client.send('NICK'.encode('ascii'))  # Requesting the nickname 
    
    if nickname == 'admin':
      client.send('PASS').encode('ascii'))
      password = client.recv(1024).decode('ascii')
      
      if password != 'adminpass': 
        client.send('REFUSE'.encode('ascii'))
        client.close()
        continue
        
    
    nickname = client.recv(1024).decode('ascii')  # Receiving the nickname from the client 
    
    # Appending the values to the list 
    nicknames.append(nickname)
    clients.append(client)
    
    print(f'Nickname of the client is {nickname}!')
    broadcast(f'{nickname} joined the chat!'.encode('ascii'))
    client.send('Connected to the server!'.encode('ascii'))
    
    thread = threading.Thread(target=handle, args=(client,))
    thread.start()
    
    
print("Server is listening...")
receive()
