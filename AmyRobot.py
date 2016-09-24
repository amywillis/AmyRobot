import RPi.GPIO as GPIO
import servo
import datetime
import speak
import os, struct, array
import threading
import time

from fcntl import ioctl
from grovepi import *
from grove_rgb_lcd import *



def joyControl( ):
        global running
        global remote
        #see http://docs.python.org/library/struct.html for the format determination 
        EVENT_BUTTON = 0x01 #button pressed/released 
        EVENT_AXIS = 0x02  #axis moved  
        EVENT_INIT = 0x80  #button/axis initialized  
        EVENT_FORMAT = "IhBB" 
        EVENT_SIZE = struct.calcsize(EVENT_FORMAT)
        #define the device 
        device = '/dev/input/js0'
        try: 
            # Open the joystick device.
            dev = '/dev/input/js0'
            print('Opening %s...' % dev)#hi sloths class
            jsdev = open(dev,'rb')

            # Get the device name.
            buf = array.array('c', ['\0'] * 64)
            ioctl(jsdev, 0x80006a13 + (0x10000 * len(buf)), buf) # JSIOCGNAME(len)
            js_name = buf.tostring()
            print('Device name: %s' % js_name)            
        except Exception, ex:            
            print ( ex )
        
        while running:
            try: #becoming bat cuthulu
                    evbuf = jsdev.read(8)                              
                    if evbuf:
                         seq, value, type, number = struct.unpack(EVENT_FORMAT, evbuf)
                         event = type & ~EVENT_INIT
                         init = type & ~event 
                         if event == EVENT_BUTTON: 
                              print ('Button %s %s ' % ( number, value ))
                              # Add more if number and value below for more buttons
                              if number == 3 and value == 1:
                                  speak.say("Amy and Chloe are unicorns!")
                              if number == 0 and value == 1:
                                  speak.say('Hello everyone, I am sprinkle face the robot,I have an evil army, and I plan to destroy the world')
                              if number == 1 and value == 1:
                                  speak.say('eeeeeeeek')
                              if number == 2 and value == 1:
                                  speak.say('goodbye')
                              if number == 4 and value == 1:
                                  speak.say('Yay')
                              if number == 8 and value == 1:
                                  running = False
                              if number == 9 and value == 1:
                                  remote = not remote                                  
                                  servo.servo_stop()

                         # Only process access events if remote control is enabled         
                         if event == EVENT_AXIS and remote: 
                              axis = number
                              if axis == 1:
                                      if value < 0 :
                                              print('left Forwards')
                                              servo.servo_left_forward()
                                      elif value > 0:
                                              print('left Backwards')
                                              servo.servo_left_backward()
                                      else :
                                              print('stop')
                                              servo.servo_stop()  
                              elif axis == 3:
                                      if value < 0 :
                                              print('right Forwards')
                                              servo.servo_right_forward()
                                      elif value > 0:
                                              print('right Backwards')
                                              servo.servo_right_backward()
                                      else :
                                              print('stop')
                                              servo.servo_stop()
            except KeyboardInterrupt:
                    return


            except Exception, ex:            
                    print ( ex )
                        
        

global running
global remote                   
try:
        ultrasonic_ranger = 7
        servo.servo_init()
        setRGB(255,138,150)
        setText("    ")

        remote = True        
        running = True

        # start a new thread to look after the joy stick
        t = threading.Thread(target=joyControl)    
        t.start()
    
        while running:                
                
                        
                #servo.servo_forward()
                try:
                    dist = ultrasonicRead(ultrasonic_ranger)
                except Exception, ex:            
                    print ( ex )
            
                msg = " Distance = " + str(dist)
                setText(msg)                        
                
                if dist < 8 :                        
                        setText(" Eeeeek!")
                        #speak.say("Eeeeeeeek!")                        
                        #servo.servo_backward()
                        time.sleep(1)
                        #servo.servo_right()
                        time.sleep(1)
                        #servo.servo_stop()
                        
                time.sleep(0.01)

except KeyboardInterrupt:
    print
    pass

finally:        
        servo.servo_cleanup()
        setText(" Goodbye")        
