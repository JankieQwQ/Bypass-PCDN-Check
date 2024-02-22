import socket
import random

def nslookup(domain):
    try:
        ip_addresses = socket.gethostbyname_ex(domain)[-1]
        return ip_addresses
    except socket.gaierror as e:
        return [str(e)]

def main():
    domain = 'awaland.xyz' # A cloudflare proxy domain
    ip_list = nslookup(domain)
    size = random.randint(1,10)
    for i in range(1024):
        try:
            for host in ip_list:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((host, 80))
                data = b'0' * size * 1024 * 1024 
                sock.sendall(data)
                sock.close()
        except Exception as e:
            print(e)

if __name__ == '__main__':
    print('PCDN CHECK BYPASSER')
    print('Use Ctrl-C Return to exit.')
    try:
        while True:
            main()
    except KeyboardInterrupt:
        pass