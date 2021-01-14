#!/bin/python3

import joystick_mapping as mapping;

import pygame
import time
import threading
import sys

#implemented with the help of https://www.pygame.org/docs/ref/joystick.html
class Gamepad:
    def __init__(self):
        self.A = 0;
        self.B = 0;
        self.X = 0;
        self.Y = 0;
        self.DPAD_UP = 0;
        self.DPAD_DOWN = 0;
        self.DPAD_LEFT = 0;
        self.DPAD_RIGHT = 0;
        self.LEFT_BUMPER = 0;
        self.RIGHT_BUMPER = 0;
        self.LEFT_STICK_PRESSED = 0;
        self.RIGHT_STICK_PRESSED = 0;
        self.LEFT_TRIGGER = float(0);
        self.RIGHT_TRIGGER = float(0);
        self.LEFT_STICK_X = float(0);
        self.LEFT_STICK_Y = float(0);
        self.RIGHT_STICK_X = float(0);
        self.RIGHT_STICK_Y = float(0);
        self.BACK = 0;
        self.START = 0;
        self.GUIDE = 0;
        
        pygame.init();
            
    
        pygame.display.init()
        pygame.joystick.init()
    
        joystick_count = pygame.joystick.get_count();
        if joystick_count == 0:
            sys.exit("ERROR no joystick detected");
       
        joysticks = [];
    
        print("detected " + str(joystick_count))
        print("This will cycle through them all with a delay of 3s.");
        print("Hold the A button on your gamepad when its name shows up until the script tells you to release it");
    
        idx = -1;
    
        for i in range(0,joystick_count):
            self.gamepad = pygame.joystick.Joystick(i);
            self.gamepad.init();
            print("Trying joystick " + str(i));
            time.sleep(3);
            pygame.event.pump();
            if self.gamepad.get_button(mapping.A_BUTTON) == 1:
                print("gamepad initialized");
                idx = i;
                break;
            self.gamepad.quit();
        
        if idx == -1:
            sys.exit("ERROR no gamepad could be determined");

    def update_inputs(self):
        pygame.event.pump();
        
        self.A = self.gamepad.get_button(mapping.A_BUTTON);
        self.B = self.gamepad.get_button(mapping.B_BUTTON);
        self.X = self.gamepad.get_button(mapping.X_BUTTON);
        self.Y = self.gamepad.get_button(mapping.Y_BUTTON);

        self.DPAD_UP = 1 if self.gamepad.get_hat(0)[1] == 1 else 0;
        self.DPAD_DOWN = 1 if self.gamepad.get_hat(0)[1] == -1 else 0;
        self.DPAD_LEFT = 1 if self.gamepad.get_hat(0)[0] == -1 else 0;
        self.DPAD_RIGHT = 1 if self.gamepad.get_hat(0)[0] == 1 else 0;
        
        self.LEFT_BUMPER = self.gamepad.get_button(mapping.LEFT_BUMPER_BUTTON);
        self.RIGHT_BUMPER = self.gamepad.get_button(mapping.RIGHT_BUMPER_BUTTON);
        self.LEFT_STICK_PRESSED = self.gamepad.get_button(mapping.LEFT_STICK_BUTTON);
        self.RIGHT_STICK_PRESSED = self.gamepad.get_button(mapping.RIGHT_STICK_BUTTON);
 
        self.LEFT_TRIGGER = (self.gamepad.get_axis(mapping.LEFT_TRIGGER_AXIS) - mapping.LEFT_TRIGGER_LOW) / (mapping.LEFT_TRIGGER_HIGH - mapping.LEFT_TRIGGER_LOW);
        self.RIGHT_TRIGGER = (self.gamepad.get_axis(mapping.RIGHT_TRIGGER_AXIS) - mapping.RIGHT_TRIGGER_LOW) / (mapping.RIGHT_TRIGGER_HIGH - mapping.RIGHT_TRIGGER_LOW);

        self.LEFT_STICK_X = self.gamepad.get_axis(mapping.LEFT_STICK_X_AXIS);
        self.LEFT_STICK_Y = self.gamepad.get_axis(mapping.LEFT_STICK_Y_AXIS) * (1 if mapping.INVERT_Y_AXIS == False else -1);
        self.RIGHT_STICK_X = self.gamepad.get_axis(mapping.RIGHT_STICK_X_AXIS);
        self.RIGHT_STICK_Y = self.gamepad.get_axis(mapping.RIGHT_STICK_Y_AXIS) * (1 if mapping.INVERT_Y_AXIS == False else -1);
        
        self.BACK = self.gamepad.get_button(mapping.BACK_BUTTON);
        self.START = self.gamepad.get_button(mapping.START_BUTTON);
        self.GUIDE = self.gamepad.get_button(mapping.GUIDE_BUTTON);
    
    def get_transmission_message(self):
        message_components = [];
        message_components.append("A~" + str(self.A));
        message_components.append("B~" + str(self.B));
        message_components.append("X~" + str(self.X));
        message_components.append("Y~" + str(self.Y));
        
        message_components.append("D_UP~" + str(self.DPAD_UP));
        message_components.append("D_DN~" + str(self.DPAD_DOWN));
        message_components.append("D_LT~" + str(self.DPAD_LEFT));
        message_components.append("D_RT~" + str(self.DPAD_RIGHT));
        
        message_components.append("L_BMP~" + str(self.LEFT_BUMPER));
        message_components.append("R_BMP~" + str(self.RIGHT_BUMPER));
        message_components.append("L_PRS~" + str(self.LEFT_STICK_PRESSED));
        message_components.append("R_PRS~" + str(self.RIGHT_STICK_PRESSED));
        
        message_components.append("L_TRG~" + str(self.LEFT_TRIGGER));
        message_components.append("R_TRG~" + str(self.RIGHT_TRIGGER));


        message_components.append("L_X~" + str(self.LEFT_STICK_X));
        message_components.append("L_Y~" + str(self.LEFT_STICK_Y));
        message_components.append("R_X~" + str(self.RIGHT_STICK_X));
        message_components.append("R_Y~" + str(self.RIGHT_STICK_Y));
        
        message_components.append("BACK~" + str(self.BACK));
        message_components.append("START~" + str(self.START));
        message_components.append("GUIDE~" + str(self.GUIDE));

        msg = message_components[0];

        for i in range(1,len(message_components)):
            msg = msg + "," + message_components[i];

        return msg;

