import threading
import socket
nickname = ''
host = ''
port = 0

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)

        except:
            print('An errie ocurred')
            client.close()
            break



def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))


receiver_thread = threading.Thread(target=receive)
receiver_thread.start()


writer_thread = threading.Thread(target=write)
writer_thread.start()