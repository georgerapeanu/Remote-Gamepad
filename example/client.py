#!/bin/python3

import socket
import threading

HEADER = 64;
FORMAT = "utf-8";
PORT = 6969;
DISCONNECT_MESSAGE = "!DISCONNECT";
SERVER = "127.0.1.1"
#SERVER = "109.100.16.101"

ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
client.connect(ADDR);

def send(msg):
    message = msg.encode(FORMAT);
    msg_length = len(message);
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length));
    client.send(send_length);
    client.send(message);

send("HELLO");
send(DISCONNECT_MESSAGE);
#send(DISCONNECT_MESSAGE);
