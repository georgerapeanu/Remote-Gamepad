#!/bin/python3
import environmental_variables as __env; 

import socket;
import time;
import threading;
import Gamepad;
import sys;

#This runs on a separate thread and insures that all server messages will be printed to the driver
#Server messages dont actually affect the client behavior, so they can just be printed while the actual client code is running
def handle_server_messages(driver):
    while True:
        msg = driver.recv(__env.MAX_MESSAGE_SIZE).decode(__env.FORMAT);
        print(msg);
        if msg == __env.DISCONNECT:
            return;

def start():
    #setting up our gamepad interface
    gamepad = Gamepad.Gamepad();

    #establishing a TCP connection to the server
    driver = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
    driver.connect(__env.HOST);


    #Checking if the server threw an error and disconects if thats the case
    connect_msg = driver.recv(__env.MAX_MESSAGE_SIZE).decode(__env.FORMAT);

    print(connect_msg);
    
    if connect_msg in __env.ERROR_MESSAGES:
        return ;
    
    #starting the server messages thread.
    thread = threading.Thread(target=handle_server_messages,args = [driver]);
    thread.start();


    print("driver connected at ",__env.HOST);

    #To prevent spamming the server and causing undefined behavior, we are only sending the input message when the actual input state changes,
    #with a delay of 10ms between messages.
    #However, since we are using UDP to communicate with the robot, there is a slight chance of packet loss
    #To prevent that, the client will resend the message if a second has passed since it last sent one
    last_transmission_message = "";
    last_time = time.time() - 20;

    while True:
        time.sleep(0.01);
        gamepad.update_inputs();
        message = gamepad.get_transmission_message();
        if message != last_transmission_message or (time.time() - last_time >= 1):
            last_transmission_message = message;
            last_time = time.time();
            driver.send(message.encode(__env.FORMAT));

start();
