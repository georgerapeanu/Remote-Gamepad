#!/bin/python3

import pygame
import time
import threading
import sys

TIME_INTERVAL = 3;

def get_pressed_buttons(gamepad):
    pygame.event.pump();
    ans = [];
    for i in range(0,gamepad.get_numbuttons()):
        if gamepad.get_button(i):
            ans.append(i);
    return ans;
def get_active_axes(gamepad,default_values):
    pygame.event.pump();
    ans = [];
    for i in range(0,gamepad.get_numaxes()):
        #print(i,gamepad.get_axis(i),default_values[i]);
        if abs(gamepad.get_axis(i) - default_values[i]) > 1e-4:
            ans.append((i,gamepad.get_axis(i)));
    return ans;

def main():
    pygame.init();
            
    
    pygame.display.init()
    pygame.joystick.init()
    
    joystick_count = pygame.joystick.get_count();
    
    if joystick_count == 0:
        sys.exit("ERROR no joystick detected");
    
    
    print("detected " + str(joystick_count))
    print("This will cycle through them all with a delay of " + str(TIME_INTERVAL) + "s.");
    print("Hold the A button on your gamepad when its name shows up until the script tells you to release it");
 
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
        
    if idx == -1:
        sys.exit("ERROR no gamepad could be determined");
   
    pygame.event.pump();
    default_values = [];
    for i in range(0,gamepad.get_numaxes()):
        default_values.append(gamepad.get_axis(i));

    time.sleep(TIME_INTERVAL);

    f = open("joystick_mapping.py","w");

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
            f.write("INVERT_Y_AXIS = " + ("True" if a[0][1] < 0 else "False") + "\n");
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
