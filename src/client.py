import urllib.request
import _thread
import random

def send():
    while True:
        try:
            pic = urllib.request.urlopen('https://img.alicdn.com/imgextra/i1/O1CN01xA4P9S1JsW2WEg0e1_!!6000000001084-2-tps-2880-560.png?{}'.format(str(ranom.random())))
            del pic
        except:
            send()

def main():
    for i in range(1024):
        try:
            _thread.start_new(send, ())
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
