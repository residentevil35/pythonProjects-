import socket 
import threading 

nickname = input("Choose a nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

# Receiving messages from the server 
def receive():
  while True:
    try:
      message = client.recv(1024).decode('ascii')
      if message == 'NICK':
        client.send(nickname.encode('ascii'))
      else:
        print(message)
    except:
      print("An error occurred!")
      client.close()
      break
 
# Encodes the client's message and sends to the server 
def write():
  while True:
    message = f'{nickname}: {input("")}'
    client.send(message.encode('ascii'))
    
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_htread.start()
