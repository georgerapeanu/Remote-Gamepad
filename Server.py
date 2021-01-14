#!/bin/python3

import environmental_variables as __env; 

import socket;
import threading;
import os;
import sys;

TIMEOUT_DURATION = 2;

host = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
host.bind(("0.0.0.0",__env.HOST_PORT));

robot = socket.socket(socket.AF_INET,socket.SOCK_DGRAM);

available_driver_spots = [False,True,True];

def handle_client(conn,addr):
    print("attempted connection ",addr);
    if addr[0] not in __env.DRIVER_ADDRESSES:
        print("address not recognized, connection failed");
        conn.send(__env.ERROR_MESSAGES[1].encode(__env.FORMAT));
    else:
        driver_id = -1;
        for i in range(0,len(available_driver_spots)):
            if available_driver_spots[i] == True:
                driver_id = i;
                available_driver_spots[i] = False;
                break;
        if driver_id == -1:
            conn.send(__env.ERROR_MESSAGES[0].encode(__env.FORMAT));
            return ;

        print("driver " + str(driver_id) + " connected at " + str(addr));
        conn.send(str("welcome driver #" + str(driver_id)).encode(__env.FORMAT));
        conn.settimeout(TIMEOUT_DURATION);
        connected = True;

        while connected:
            try:
                msg = conn.recv(__env.MAX_MESSAGE_SIZE).decode(__env.FORMAT);
            except socket.timeout:
                connected = False;
                print("Driver " + str(driver_id) + " disconnected");
                available_driver_spots[driver_id] = True;
                break;

            if connected == False:
                break;

            promoted = False;

            for i in range(0,driver_id):
                if available_driver_spots[i] == True:
                    avialable_driver_spots[i] = False;
                    avialable_driver_spots[driver_id] = True;
                    driver_id = i;
                    promoted = True;
                    break;
            if promoted:
                conn.send(("Promoted to driver #" + str(driver_id)).encode(__env.FORMAT));

            if len(msg) > 0:
                msg = "G~" + str(driver_id) + "," + msg;
                print("recieved following command ");
                print(msg);
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
