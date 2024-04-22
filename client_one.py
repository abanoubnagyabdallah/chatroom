import socket
import threading

host = socket.gethostname()
port = 12345
serv_add=(host,port)
cli=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cli.connect(serv_add)
nickname=input('Enter your name :')

def send():
    while True:
        try:
            msg = nickname + ' : ' + input()
            cli.sendall(msg.encode())
        except:
            print('Send Error')


def receive():
    while True:
        try:
            msg = cli.recv(1024)
            if msg == 'Nick':
                cli.send(nickname.encode())
            else:
                print(msg.decode())
        except:
            print('receive Error')
            cli.close()
            break



thread_send = threading.Thread(target=send,args=())
thread_send.start()

thread_receive = threading.Thread(target=receive,args=())
thread_receive.start()


