import socket

#message format will have the following format


FORMAT = "utf-8";
#host port over the internet
HOST_PORT = 6969

#ip address(public for remote, local for hosting)
HOST_IP = socket.gethostbyname(socket.gethostname())
#HOST_IP = "";

HOST = (HOST_IP,HOST_PORT);

DISCONNECT = "!DISCONNECT";

MAX_MESSAGE_SIZE = 1024;

ERROR_MESSAGES = ["Too many drivers, connection failed", "Address not recognized, connection failed",""];
