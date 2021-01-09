#!/bin/python3
import environmental_variables as __env; 

import socket;
import time;
import threading;
import Gamepad;

#TODO resend message after a certain time because of udp shit and packet loss 

def start():
    gamepad = Gamepad.Gamepad();

    driver = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
    driver.connect(__env.HOST);
    connect_msg = driver.recv(__env.MAX_MESSAGE_SIZE).decode(__env.FORMAT);

    print(connect_msg);
    
    if connect_msg in __env.ERROR_MESSAGES:
        return ;

    print("driver connected at ",__env.HOST);

    last_transmission_message = "";

    while True:
        time.sleep(0.01);
        gamepad.update_inputs();
        message = gamepad.get_transmission_message();
        if message != last_transmission_message:
            last_transmission_message = message;
            driver.send(message.encode(__env.FORMAT));

start();
