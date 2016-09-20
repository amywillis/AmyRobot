import RPi.GPIO as GPIO
import time
import servo
import datetime
import speak

from grovepi import *
from grove_rgb_lcd import *
  
try:
        ultrasonic_ranger = 7
        servo.servo_init()
        setRGB(255,138,150)
        setText("    ")

        previous_time = datetime.datetime.now()        
        while True:
                servo.servo_forward()
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
                        servo.servo_backward()
                        time.sleep(1)
                        servo.servo_right()
                        time.sleep(1)
                        servo.servo_stop()

                time.sleep(0.01)

except KeyboardInterrupt:
    print
    pass

finally:        
        servo.servo_cleanup()
        setText(" Goodbye")        
