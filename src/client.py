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

class config:
    def __init__(self,filename='data.csv'):
        self.filename = filename

    def write(text):
        with open(self.filename,'w') as writer:
            writer.write(text)

    def read():
        answer = ''
        with open(self.filename,'r') as reader:
            answer = reader.read()
        return answer

if __name__ == '__main__':
    print('PCDN CHECK BYPASSER')
    print('Use Ctrl-C Return to exit.')
    
    limit = 0
    limit_file = config()
    try: limit = limit_file.read()
    except:
        temp_limit = int(int(input('Please enter the flow limit(Mbps):')) * 0.0625 + 1)
        limit_file.write(str(temp_limit))
        limit = temp_limit
    bypasser = request(limit)
    
    while True:
        try:
            bypasser.main()
        except KeyboardInterrupt:
            break
    raise SystemExit(0)
