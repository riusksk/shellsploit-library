from __future__ import print_function
from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM, SOL_SOCKET, SO_REUSEADDR
from threading import Thread
from select import select
from time import sleep
from sys import exit

listening   = False
clisock     = None
done        = False

#Beta script for listener.
#Same effect nc -vlp [PORT]


#Greetz:
#Goodies
#https://twitter.com/GoodiesHQ



try:
    input = raw_input 
except NameError:
    pass 

def listen(port=4444):
    global clisock, listening, done
    s   = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', port))
    s.listen(3)
    listening   = True
    sock, addr  = s.accept()
    clisock     = sock
    print(f"Client connected from {addr}")
    data = ""
    while listening:
        try:
            rr, _, _ = select([sock,], [], [], 1)
            if rr:
                data = sock.recv(1024)
                print(f"{data}", end="")
        except:
            exit()
    print("Done listening.")
    done = True

def write():
    global clisock, listening, done
    while True:
        if clisock:
            data = input()
            if data.strip().lower() in ["exit", "quit"]:
                clisock.close()
                exit()
                listening = False
                while not done: sleep(0.1)
                break
            _, wr, _ = select([], [clisock,], [], 1)
            if wr:
                clisock.sendall(data + "\n")


def nc( PORT=4444):
    listenThread    = Thread(target=listen, args=(int(PORT),))
    writeThread     = Thread(target=write)
    listenThread.start()
    writeThread.start()
