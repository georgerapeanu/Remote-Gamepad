#!/bin/python3

import socket
import threading

HEADER = 64;
FORMAT = "utf-8";
PORT = 6969;
DISCONNECT_MESSAGE = "!DISCONNECT";
SERVER = socket.gethostbyname(socket.gethostname())
#SERVER = "109.100.16.101"

ADDR = (SERVER,PORT)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
print(ADDR);
server.bind(ADDR);

def handle_client(conn,addr):
    print("connected ",conn,addr)
    connected = True;

    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT);
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT);
            print(addr," ",msg); 
            if DISCONNECT_MESSAGE == msg:
                connected = False;

    conn.close();

def start():
    server.listen();
    print("listening on ",SERVER,PORT);
    while True:
        conn,addr = server.accept();
        thread = threading.Thread(target=handle_client, args = (conn,addr));
        thread.start();
        print("active connections:",threading.activeCount() - 1);
        
print("STARTING");
start();
