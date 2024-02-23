import socket
import multiprocessing
import random

class request:
    def __init__(self,processingNumber:int) -> None:
        self.processingNumber = processingNumber

    def send_request():
        while True:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                sock.connect(('img.alicdn.com', 80))
                request = 'GET /imgextra/i1/O1CN01xA4P9S1JsW2WEg0e1_!!6000000001084-2-tps-2880-560.png?{} HTTP/1.1\r\nHost: img.alicdn.com\r\nConnection: close\r\n\r\n'.format(random.random())
                sock.sendall(request.encode())
                response = sock.recv(1024)
                sock.close()
            except:
                send_request()

    def main(self):
        for i in range(self.processingNumber):
            try:
                process = multiprocessing.Process(target=send_request)
                process.start()
            except Exception as e:
                print(e)

if __name__ == '__main__':
    print('PCDN CHECK BYPASSER')
    print('Use Ctrl-C Return to exit.')
    should = 0
    try:
        config = open('limit.csv','r')
        should = int(config.read())
    except:
        limits = int(input('Please enter the maximum flow rate(Mbps):'))
        limits = (limits / 8 / 2) + 2
        with open('limit.csv','w') as configWriter:
            configWriter.write(str(limits))
        should = limits
    while True:
        try:
            main(should)
        except KeyboardInterrupt:
            break
    raise SystemExit(0)
