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
            print('Opening %s...' % dev)
            jsdev = open(dev,'rb')

            # Get the device name.
            buf = array.array('c', ['\0'] * 64)
            ioctl(jsdev, 0x80006a13 + (0x10000 * len(buf)), buf) # JSIOCGNAME(len)
            js_name = buf.tostring()
            print('Device name: %s' % js_name)            
        except Exception, ex:            
            print ( ex )
            
        while True:
            evbuf = jsdev.read(8)
            if evbuf:
                 seq, value, type, number = struct.unpack('IhBB', evbuf)
                 #if type & 0x01:
                 #        return
                 if type & 0x02:
                      axis = number
                      fvalue = value / 32767.0
                      #print "%s: %.3f" % (axis, fvalue)
                      if axis == 1:
                              if fvalue < 0 :
                                      print('left Forwards')
                                      servo.servo_forward()
                              elif fvalue > 0:
                                      print('left Backwards')
                                      servo.servo_backward()
                              else :
                                      print('stop')
                                      servo.servo_stop()  
                      elif axis == 3:
                              if fvalue < 0 :
                                      print('right Forwards')
                                      servo.servo_forward()
                              elif fvalue > 0:
                                      print('right Backwards')
                                      servo.servo_backward()
                              else :
                                      print('stop')
                                      servo.servo_stop()
            
                        
        
                   
try:
        ultrasonic_ranger = 7
        servo.servo_init()
        setRGB(255,138,150)
        setText("    ")              

        # start a new thread to look after the joy stick
        t = threading.Thread(target=joyControl)    
        t.start()
    
        previous_time = datetime.datetime.now()        
        while True:                
                
                        
                #servo.servo_forward()
                dist = ultrasonicRead(ultrasonic_ranger)
        
                if datetime.datetime.now() > ( previous_time + datetime.timedelta(seconds = 15 )):
                        setRGB(255,100,100)
                        setText(" Amy and Chloe   are unicorns!")
                        speak.say("Amy and Chloe are unicorns!")
                        setRGB(255,138,150)
                        previous_time = datetime.datetime.now() 
                else :                        
                        msg = " Distance = " + str(dist)
                        setText(msg)                        
                
                if dist < 8 :                        
                        setText(" Eeeeek!")
                        speak.say("Eeeeeeeek!")                        
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
