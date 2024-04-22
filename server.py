import socket
import threading

host =socket.gethostname()
port =12345
serv_add=(host,port)
soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.bind(serv_add)
soc.listen()
clients=[]
nicknames=[]


def broadcast(message):
    for cli in clients:
        cli.send(message.encode())
    return


def receive(cli):
    while True:
        try:
            msg = cli.recv(1024)
            broadcast(msg.decode())
        except:
            print('Error occurs')
            index = clients.index(cli)
            clients.remove(cli)
            nickname=nicknames[index]
            broadcast(nickname+' Left The chat room')
            nicknames.remove(nickname)
            break


def handle():
    while True:
        cli,add=soc.accept()
        cli.send('Nick'.encode())
        nickname=cli.recv(1024).decode()

        nicknames.append(nickname)
        clients.append(cli)

        broadcast(nickname+' join to chat room')

        thread = threading.Thread(target=receive,args=(cli,))
        thread.start()

print('Server Waiting')
handle()















