'''
Title  : s51servo.py
Author : Shane Shankar
Date   : 4/21/24
Purpose: Contains the s51_servo class for our ECE 1000 project, a robot arm.
         could use more polish, but I'm not lazy just busy I Shane Shanker am a genius.
'''
from machine import Pin,PWM

class s51_servo:
    
    
    def __init__(self, pin : int or Pin or PWM, minval = 2000, maxval = 8000, pos = 5000): # weird numbers based on testing the range of the servos. Amazon Lied.
        # If statements that to make sure different pin inputs are valid for use.
        if isinstance(pin, int):
            pin = Pin(pin, Pin.OUT)
        if isinstance(pin, Pin):
            self.__pwm = PWM(pin)
        if isinstance(pin, PWM):
            self.__pwm = pin
        
        # Setting values for instance members and frequency
        self.maxval = maxval
        self.minval = minval
        self.pos = pos
        self.__pwm.freq(50)
        
        
    #Deconstructor
    def __deinit__():
        self.__pwm.deinit()
        
        
    def move(self, uInput : int):
        # increments or decrements pos by an input value
        self.pos  = (self.pos + uInput)
        # sets pos back to maxval if pos goes above maxval
        if self.pos > self.maxval:
            self.pos = self.maxval
            
        #sets pos back to minval if pos goes below minval
        if self.pos < self.minval:
            self.pos = self.minval
        # movement of servo
        self.__pwm.duty_u16(self.pos)
        

        
    # a reset function that was never used
    def reset(self):
        
        self.move(5000)
        self.pos = 5000
        
        

        
            
        
    
        
        
        
            
        
    
