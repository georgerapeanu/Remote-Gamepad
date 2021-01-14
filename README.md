# RemoteDrive

Enables remote Driver-Controlled TeleOp over the internet for FIRST Tech Challenge teams.

# About RemoteDrive

The COVID-19 pandemic left FIRST Tech Challenge competitions in a weird place: due to local restriction, teams might not be able to all meet up and work and control the robot. There are many teams who mainly use online application like Google Meet, Discord or Zoom, but getting the robot to be able to be controlled remotely is tricky. This project's purpose is to make this remote control feature available and easily accessible to any FTC team.

Our measurements indicate that the worst case latency of this project is about 50ms, but normally it performs much better.

# Installation, Setup, and Usage

  ### Part 1: Replace all ```LinearOpMode``` inheritances with ```RemoteDrive``` inheritances. 
  
  1. Simply download ```RemoteDrive.java```, and copy it into your ```TeamCode``` folder
  2. Change your TeleOp program(s) to extend the ```RemoteDrive``` class
  3. In your ```runOpMode``` method you should call ```super._init()``` in the beginning of the method, ```super.after_start()``` after the ```LinearOpMode``` has started and ```super._end()``` before the ```LinearOpMode``` ends;
  4. Using your Driver Station phone, navigate to the "Program and Manage" menu, and find the local IP address of the Control Hub or Robot Controller phone
  5. On line 174 in ```RemoteDrive.java```, replace the existing IP address with the IP address you found in Step 4
  6. Optional: change the local port in ```RemoteDrive.java``` at line 174 (default is 6969). You should also change this in ```environmental_variables.py```
  Checkout ```test_001.java``` to see exacly how this is done
  
  ### Part 2: Setup the Host Computer (a computer that's in the same physical location as the robot)

  1. On the Host Computer, you should install the following software:
* Zerotier(https://www.zerotier.com/download/)
* Python3(https://www.python.org/downloads/) - make sure to add it to PATH
* Pip3(https://pip.pypa.io/en/stable/installing/) - make sure to add it to PATH
* The following pip3 modules: ```socket```, ```threading```, ```os```, ```sys```, ```time```, ```pygame```(some of them might come with the default python installer) 
  2. Plug in a USB WiFi adapter/Ethernet Cable to the Host Computer
  3. Connect the one Wifi to the Control Hub or Robot Controller, and ensure that the other internet connection is connected to your local router
  4. Here you have two options for making this computer discoverable by the drivers:

    ###### Method 1: Port Forwarding
    You should choose a port on which you want the server on the host computer to run. You must forward this port to the router so it becomes accessible over the internet. After that, you should  Edit ```environmental_variables.py``` accordingly.(More exactly you should modify the ROBOT_ADDRESS(the ip used in ```RemoteDrive.java```),ROBOT_PORT(the port used in ```RemoteDrive.java```),HOST_ADDRESS(the public ip of the host),HOST_PORT(the forwarded port) and DRIVER_ADDRESSES(the public ip of the drivers)).

    ###### Method 2: Zerotier
    You should log into zerotier and create a network. After that you should connect to that network with the host and drivers computers. After that, you should  Edit ```environmental_variables.py``` accordingly.(More exactly you should modify the ROBOT_ADDRESS(the ip used in ```RemoteDrive.java```),ROBOT_PORT(the port used in ```RemoteDrive.java```),HOST_ADDRESS(the zerotier ip of the host),HOST_PORT(the port used to run the server) and DRIVER_ADDRESSES(the public ip of the drivers)).

  5. Open a terminal/command prompt window and type ```python3 Server.py```

  Now, your host is ready to recieve commands from the Driver Computers(s).

  ### Part 4: Setup the Driver Computer (a computer that is used to remotely control the robot)
  
 1. On the Driver Computer, you should install the following software:
    * Zerotier(https://www.zerotier.com/download/)
    * Python3(https://www.python.org/downloads/)
    * Pip3(https://pip.pypa.io/en/stable/installing/)
    * The following pip3 modules: ```socket```, ```threading```, ```os```, ```sys```, ```time```, ```pygame```(some of them might come with the default python installer) 
 2. Plug in a USB gamepad (ex. Logitech F310). 
 3. Open a terminal/command prompt window in the current directory. type "python3 Config.py". This should configure your local variant of this project to work correctly with your gamepad. - this can be done as many times as you like, but it is necessary to do it only once before the first use of this project.
 4. Edit ```environmental_varialbles.py``` accordingly(More exactly you should modify the HOST_ADDRESS(the public ip / zerotier ip) and HOST_PORT(the port used by the host to run the server)
 5. In the same terminal/ command prompt window, type ```python3 Client.py```. Your driver computer should now succesfully send commands to the server computer(you can verify this by seeing some messages on the server terminal).

# Common Errors

  ### Port ____ is currently in use on your machine. Please try a different port.

This is most likely the only error you would encounter. In this case, you must change the the Host Port to another integer number as the Host computer is already using that port for another function. **Make sure you change the port on both the driver side and the host side in ```environmental_variables.py```**

  ### Something else is wrong
  
# Contributors

  ### Developers

Rapeanu George 

Lazar Mihai

### Testers

# Disclaimer:

The camera feed is handled through Google Meet, Discord or Zoom or whichever service you choose to use.
Our software does not connect to camera, it only sends the gamepad control commands over the internet.

© Architechs FTC Team RO028 | All Rights Reserved 2021
