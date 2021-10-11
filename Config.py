#!/bin/python3

#importing libraries
import pygame
import time
import threading
import sys

#the time an user has to press/release buttons
TIME_INTERVAL = 2;

#get pressed user buttons between the last and current check
def get_pressed_buttons(gamepad):
    pygame.event.pump();
    ans = [];
    for i in range(0,gamepad.get_numbuttons()):
        if gamepad.get_button(i):
            ans.append(i);
    return ans;

#gets the used axis between the last and current check
def get_active_axes(gamepad,default_values):
    pygame.event.pump();
    ans = [];
    for i in range(0,gamepad.get_numaxes()):
        #print(i,gamepad.get_axis(i),default_values[i]);
        if abs(gamepad.get_axis(i) - default_values[i]) > 5e-2:
            ans.append((i,gamepad.get_axis(i)));
    return ans;

def main():

    #intializing pygame
    pygame.init();
    pygame.display.init()
    pygame.joystick.init()
    
    #getting the number of plugged in joysticks
    joystick_count = pygame.joystick.get_count();
    
    if joystick_count == 0:
        sys.exit("ERROR no joystick detected");
    
    
    #printing user instructions
    print("detected " + str(joystick_count))
    print("This will cycle through them all with a delay of " + str(TIME_INTERVAL) + "s.");
    print("Hold the A button on your gamepad when its name shows up until the script tells you to release it");
 

    #checking all gamepads in order to detect the used one
    idx = -1;
    gamepad = "";

    for i in range(0,joystick_count):
        gamepad = pygame.joystick.Joystick(i);
        gamepad.init();
        print("Trying joystick " + str(i));
        time.sleep(TIME_INTERVAL);
        pygame.event.pump();
        if len(get_pressed_buttons(gamepad)) > 0:
            print("gamepad detected");
            idx = i;
            break;
        gamepad.quit();
    
    #if none found, throw an error
    if idx == -1:
        sys.exit("ERROR no gamepad could be determined");
   
    #getting the default values of all gamepad inputs
    pygame.event.pump();
    default_values = [];
    for i in range(0,gamepad.get_numaxes()):
        default_values.append(gamepad.get_axis(i));

    time.sleep(TIME_INTERVAL);

    #opening the config file
    f = open("joystick_mapping.py","w");

    #promptin user with instructions for configuring all buttons and axis
    print("\n");
    print("Press the A button on your gamepad...\n")

    while(True):
        time.sleep(0.1);
        a = get_pressed_buttons(gamepad);
        if len(a) == 1:
            f.write("A_BUTTON = " + str(a[0]) + "\n");
            break;
    print("Release the A button on your gamepad...\n");
    time.sleep(TIME_INTERVAL);

    print("Press the B button on your gamepad...\n")

    while(True):
        time.sleep(0.1);
        a = get_pressed_buttons(gamepad);
        if len(a) == 1:
            f.write("B_BUTTON = " + str(a[0]) + "\n");
            break;
    print("Release the B button on your gamepad...\n");
    time.sleep(TIME_INTERVAL);
    
    print("Press the X button on your gamepad...\n")

    while(True):
        time.sleep(0.1);
        a = get_pressed_buttons(gamepad);
        if len(a) == 1:
            f.write("X_BUTTON = " + str(a[0]) + "\n");
            break;
    
    print("Release the X button on your gamepad...\n");
    time.sleep(TIME_INTERVAL);

    print("Press the Y button on your gamepad...\n")

    while(True):
        time.sleep(0.1);
        a = get_pressed_buttons(gamepad);
        if len(a) == 1:
            f.write("Y_BUTTON = " + str(a[0]) + "\n");
            break;

    print("Release the Y button on your gamepad...\n");
    time.sleep(TIME_INTERVAL);
    f.write("\n");

    
    print("Press the LB button on your gamepad...\n")

    while(True):
        time.sleep(0.1);
        a = get_pressed_buttons(gamepad);
        if len(a) == 1:
            f.write("LEFT_BUMPER_BUTTON = " + str(a[0]) + "\n");
            break;
    
    print("Release the LB button on your gamepad...\n");
    time.sleep(TIME_INTERVAL);
    
    print("Press the RB button on your gamepad...\n")

    while(True):
        time.sleep(0.1);
        a = get_pressed_buttons(gamepad);
        if len(a) == 1:
            f.write("RIGHT_BUMPER_BUTTON = " + str(a[0]) + "\n");
            break;
    
    print("Release the RB button on your gamepad...\n");
    time.sleep(TIME_INTERVAL);

    print("Press the LS button on your gamepad...\n")

    while(True):
        time.sleep(0.1);
        a = get_pressed_buttons(gamepad);
        if len(a) == 1:
            f.write("LEFT_STICK_BUTTON = " + str(a[0]) + "\n");
            break;
    
    print("Release the LS button on your gamepad...\n");
    time.sleep(TIME_INTERVAL);
        
    print("Press the RS button on your gamepad...\n")

    while(True):
        time.sleep(0.1);
        a = get_pressed_buttons(gamepad);
        if len(a) == 1:
            f.write("RIGHT_STICK_BUTTON = " + str(a[0]) + "\n");
            break;

    f.write("\n");

    print("Release the RS button on your gamepad...\n");
    time.sleep(TIME_INTERVAL);
    
    print("Press the START button on your gamepad...\n")

    while(True):
        time.sleep(0.1);
        a = get_pressed_buttons(gamepad);
        if len(a) == 1:
            f.write("START_BUTTON = " + str(a[0]) + "\n");
            break;
    
    print("Release the START button on your gamepad...\n");
    time.sleep(TIME_INTERVAL);
    

    print("Press the BACK button on your gamepad...\n")

    while(True):
        time.sleep(0.1);
        a = get_pressed_buttons(gamepad);
        if len(a) == 1:
            f.write("BACK_BUTTON = " + str(a[0]) + "\n");
            break;
    
    print("Release the BACK button on your gamepad...\n");
    time.sleep(TIME_INTERVAL);
    
    print("Press the GUIDE button on your gamepad...\n")

    while(True):
        time.sleep(0.1);
        a = get_pressed_buttons(gamepad);
        if len(a) == 1:
            f.write("GUIDE_BUTTON = " + str(a[0]) + "\n");
            break;

    f.write("\n");
    
    print("Release the GUIDE button on your gamepad...\n");
    time.sleep(TIME_INTERVAL);
    

    print("Move your left stick to the right...\n");

    while(True):
        time.sleep(0.1);
        a = get_active_axes(gamepad,default_values);
        if len(a) == 1:
            f.write("INVERT_X_AXIS = " + ("True" if a[0][1] < 0 else "False") + "\n");
            f.write("LEFT_STICK_X_AXIS = " + str(a[0][0]) + "\n");
            break;
    
    print("Release the left stick...\n");
    time.sleep(TIME_INTERVAL);

    print("Move your left stick up...\n");

    while(True):
        time.sleep(0.1);
        a = get_active_axes(gamepad,default_values);
        if len(a) == 1:
            f.write("LEFT_STICK_Y_AXIS = " + str(a[0][0]) + "\n");
            f.write("INVERT_Y_AXIS = " + ("True" if a[0][1] > 0 else "False") + "\n");
            break;

    print("Release the left stick...\n");
    time.sleep(TIME_INTERVAL);
    
    print("Move your right stick to the right...\n");

    while(True):
        time.sleep(0.1);
        a = get_active_axes(gamepad,default_values);
        if len(a) == 1:
            f.write("RIGHT_STICK_X_AXIS = " + str(a[0][0]) + "\n");
            break;
    
    print("Release the right stick...\n");
    time.sleep(TIME_INTERVAL);

    print("Move your right stick up...\n");

    while(True):
        time.sleep(0.1);
        a = get_active_axes(gamepad,default_values);
        if len(a) == 1:
            f.write("RIGHT_STICK_Y_AXIS = " + str(a[0][0]) + "\n");
            break;
    
    print("Release the right stick...\n");
    time.sleep(TIME_INTERVAL);
    
    print("Press your left trigger...\n");

    while(True):
        time.sleep(0.1);
        a = get_active_axes(gamepad,default_values);
        if len(a) == 1:
            f.write("LEFT_TRIGGER_AXIS = " + str(a[0][0]) + "\n");
            f.write("LEFT_TRIGGER_LOW = " + str(default_values[a[0][0]]) + "\n");
            f.write("LEFT_TRIGGER_HIGH = " + str(1) + "\n");
            break;
    
    print("Release the left trigger...\n");
    time.sleep(TIME_INTERVAL);
    
    print("Press your right trigger...\n");

    while(True):
        time.sleep(0.1);
        a = get_active_axes(gamepad,default_values);
        if len(a) == 1:
            f.write("RIGHT_TRIGGER_AXIS = " + str(a[0][0]) + "\n");
            f.write("RIGHT_TRIGGER_LOW = " + str(default_values[a[0][0]]) + "\n");
            f.write("RIGHT_TRIGGER_HIGH = " + str(1) + "\n");
            break;
    
    print("Release the right trigger...\n");
    time.sleep(TIME_INTERVAL);

    f.close();

main();
