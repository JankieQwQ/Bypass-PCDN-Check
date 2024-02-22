import socket
import threading
import random

def send_request():
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            sock.connect(('img.alicdn.com', 80))
            request = b'GET /imgextra/i1/O1CN01xA4P9S1JsW2WEg0e1_!!6000000001084-2-tps-2880-560.png?' + str(random.random()).encode() + b' HTTP/1.1\r\nHost: img.alicdn.com\r\nConnection: close\r\n\r\n'
            sock.sendall(request)
            response = sock.recv(1024)
            sock.close()
        except:
            send_request()

def main():
    for i in range(1024):
        try:
            thread = threading.Thread(target=send_request)
            thread.start()
        except Exception as e:
            print(e)

if __name__ == '__main__':
    print('PCDN CHECK BYPASSER')
    print('Use Ctrl-C Return to exit.')
    while True:
        try:
            main()
        except KeyboardInterrupt:
            break
    raise SystemExit(0)
