#This file contains all variables that should be shared by the server or the client and/or need to be locally changed(thus this file is included in .gitignore)
import socket;

TIMEOUT_DURATION = 2;#The amount of seconds that the server waits to receive a new packet. If it doesnt receive one, it will assume that the driver disconnected

DRIVER_ADDRESSES = ["127.0.0.1"];#A list of all driver's ip addresses. This is a security feature used in order to prevent executing commands that are not comming from our drivers.
DRIVER_COUNT = 2;    

ROBOT_ADDRESS = ""#robot WIFI-Direct ip addres, has to be the same with the one in RemoteDrive.java
ROBOT_PORT = 6969#port used to communicate with robot, has to be the same with the one in RemoteDrive.java

ROBOT = (ROBOT_ADDRESS,ROBOT_PORT);

FORMAT = "utf-8";#Message encoding, has to be the same with the one int RemoteDrive.java
HOST_PORT = 42069#host port

#Host ip address
HOST_ADDRESS = socket.gethostbyname(socket.gethostname()) #This should be used when running in LAN, mainly for testing
#HOST_ADDRESS = ""; #This should be the host's public address

HOST = (HOST_ADDRESS,HOST_PORT);

DISCONNECT = "!DISCONNECT";

MAX_MESSAGE_SIZE = 1024;

ERROR_MESSAGES = ["Too many drivers, connection failed", "Address not recognized, connection failed",""];
