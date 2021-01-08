DRIVER_ADDRESSES = ["127.0.0.1"];
DRIVER_COUNT = 2;    

ROBOT_ADDRESS = ""#robot ip addres
ROBOT_PORT = 6969#port used to communicate with robot


FORMAT = "utf-8";
#host port over the internet
HOST_PORT = 42069

#ip address(public for remote, local for hosting)
#HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_IP = "109.102.5.149";

HOST = (HOST_IP,HOST_PORT);

DISCONNECT = "!DISCONNECT";

MAX_MESSAGE_SIZE = 1024;

ERROR_MESSAGES = ["Too many drivers, connection failed", "Address not recognized, connection failed",""];
