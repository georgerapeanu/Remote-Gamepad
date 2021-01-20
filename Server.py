#!/bin/python3

import environmental_variables as __env; 

import socket;
import threading;
import os;
import sys;
import time;

#Setting up the host socket
host = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
host.bind(("0.0.0.0",__env.HOST_PORT));

#Setting up the robot socket
robot = socket.socket(socket.AF_INET,socket.SOCK_DGRAM);

#Keeps track of available driver spots. When a driver connects it will take the first available spot. If the first driver disconnects, the second will take its place.
available_driver_spots = [False,True,True];

#True if server is running
SERVER_RUNNING = False;

#This handles a client connection
def handle_client(conn,addr):
    global SERVER_RUNNING;
    global available_driver_spots;
    print("attempted connection ",addr);
    if addr[0] not in __env.DRIVER_ADDRESSES:#In case that the driver is not recognized we end the connection.
        print("address not recognized, connection failed");
        conn.send(__env.ERROR_MESSAGES[1].encode(__env.FORMAT));
        conn.close();
        return ;
    else:
        #Finding the first available driver spot
        driver_id = -1;
        for i in range(0,len(available_driver_spots)):
            if available_driver_spots[i] == True:
                driver_id = i;
                available_driver_spots[i] = False;
                break;
        #If no spot was found it means that we can not accept this connection because we would have too many drivers.
        if driver_id == -1:
            conn.send(__env.ERROR_MESSAGES[0].encode(__env.FORMAT));
            conn.close();
            return ;

        #Sending a welcome message to the driver and setting the timeout duration
        print("driver " + str(driver_id) + " connected at " + str(addr));
        conn.send(str("welcome driver #" + str(driver_id)).encode(__env.FORMAT));
        conn.settimeout(__env.TIMEOUT_DURATION);
        connected = True;

        buff = "";

        while connected and SERVER_RUNNING:
            try:
                #Await driver commands
                msg = conn.recv(__env.MAX_MESSAGE_SIZE).decode(__env.FORMAT);
                buff += msg;
            except socket.timeout:
                #If driver timed out we assume they disconnected, so we end the connection,free his spot(this allows the driver to reconnect and the second driver to take over)  and output a debug message
                connected = False;
                print("Driver " + str(driver_id) + " disconnected");
                available_driver_spots[driver_id] = True;

            if connected == False:
                break;

            #Checking if a previous driver disconnected so this driver can take over
            promoted = False;

            for i in range(0,driver_id):
                if available_driver_spots[i] == True:
                    avialable_driver_spots[i] = False;
                    avialable_driver_spots[driver_id] = True;
                    driver_id = i;
                    promoted = True;
                    break;

            #if this driver was promoted we let them know by sending a message
            if promoted:
                conn.send(("Promoted to driver #" + str(driver_id)).encode(__env.FORMAT));

            pieces = buff.split("|");
            buff = pieces.pop();
            #We add the final piece to our message, that being the gamepad number, and send it to the robot
            for msg in pieces:
                if len(msg) > 0:
                    msg = "G~" + str(driver_id) + "," + msg;
                    print("recieved following command ");
                    print(msg);
                    robot.sendto(msg.encode(__env.FORMAT),__env.ROBOT);

    if SERVER_RUNNING == False and connected == True:#if the connection is still active but the server is shutting down let the client know to disconnect
        conn.send(__env.DISCONNECT.encode(__env.FORMAT));
    conn.close();

def start():
    #Starting the server
    global SERVER_RUNNING;
    SERVER_RUNNING = True;
    host.listen();
    print("listening");

    while True:
        #Waiting for a new connection
        conn,addr = host.accept();   
        #When a connection established, we handle it on a separate thread in order to be able to continue accepting connections.
        thread = threading.Thread(target=handle_client,args = (conn,addr));
        thread.start();

#Starting the server
try:
    start()
except KeyboardInterrupt:
    #Cleanly shutting down the server.
    print('Interrupted')
    try:
        SERVER_RUNNING = False;
        time.sleep(__env.TIMEOUT_DURATION + 1);
        host.shutdown(socket.SHUT_RDWR)
        host.close()
        sys.exit(0)
    except SystemExit:
        os._exit(0)
