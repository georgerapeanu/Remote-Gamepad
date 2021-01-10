#!/bin/python3

#TODO establish robot communication

import environmental_variables as __env; 

import socket;
import threading;
import os;
import sys;

host = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
host.bind(("0.0.0.0",__env.HOST_PORT));

robot = socket.socket(socket.AF_INET,socket.SOCK_DGRAM);

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
                msg = "G~" + str(driver_id) + "," + msg;
                print("recieved following command ");
                print(msg);
                #if msg == __env.DISCONNECT:
                #    connected = False;
                #    print("Driver disconnected, shutting down");
                #    host.shutdown(socket.SHUT_RDWR)
                #    host.close()
                robot.sendto(msg.encode(__env.FORMAT),__env.ROBOT);
    conn.close();

def start():
    host.listen();
    print("listening");

    while True:
        conn,addr = host.accept();    
        thread = threading.Thread(target=handle_client,args = (conn,addr));
        thread.start();

try:
    start()
except KeyboardInterrupt:
    print('Interrupted')
    try:
        host.shutdown(socket.SHUT_RDWR)
        host.close()
        sys.exit(0)
    except SystemExit:
        os._exit(0)
