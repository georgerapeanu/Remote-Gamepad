#!/bin/python3

#TODO establish robot communication

import environmental_variables as __env; 

import socket;
import threading;

ROBOT_ADDRESS = ""#robot ip addres
ROBOT_PORT = 12345#port used to communicate with robot

host = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
host.bind(("0.0.0.0",__env.HOST_PORT));


def handle_client(conn,addr):
    print("attempted connection ",addr);
    if addr[0] not in __env.DRIVER_ADDRESSES:
        print("address not recognized, connection failed");
        conn.send(__env.ERROR_MESSAGES[1].encode(__env.FORMAT));

    elif threading.activeCount() - 1 > __env.DRIVER_COUNT:
        conn.send(__env.ERROR_MESSAGES[0].encode(__env.FORMAT));
    else:
        driver_id = threading.activeCount() - 1;
        print("driver " + str(driver_id) + " connected at " + str(addr));
        conn.send(str("welcome driver #" + str(driver_id)).encode(__env.FORMAT));
        connected = True;

        while connected:
            msg = conn.recv(__env.MAX_MESSAGE_SIZE).decode(__env.FORMAT);
            if len(msg):
                msg = "G" + str(driver_id) + "_" + msg;
                print("recieved following command ");
                print(msg);
                if msg == __env.DISCONNECT:
                    connected = False;
                    print("Driver disconnected, shutting down");
                    host.shutdown(socket.SHUT_RDWR)
                    host.close()
    conn.close();

def start():
    host.listen();
    print("listening");

    while True:
        conn,addr = host.accept();    
        thread = threading.Thread(target=handle_client,args = (conn,addr));
        thread.start();
start();
