#!/usr/bin/python
#
#
# Import all necessary libraries
import RPi.GPIO as GPIO, sys, threading, time, os, subprocess

# Pins 24, 26 Right Motor
# Pins 19, 21 Left Motor
R1 = 24
R2 = 26
L1 = 19
L2 = 21

# Define Sonar Pin (same pin for both Ping and Echo)
# Note that this can be either 8 or 23 on PiRoCon
sonar = 8

RUN_ON = 7

def init():
    global p, q, a, b
    # Initialise the PWM device using the default address

    #use physical pin numbering
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(RUN_ON, GPIO.IN) 
    print "Revision = ",GPIO.RPI_REVISION
    
    GPIO.setup(L1, GPIO.OUT)
    p = GPIO.PWM(L1, 20)
    p.start(0)

    GPIO.setup(L2, GPIO.OUT)
    q = GPIO.PWM(L2, 20)
    q.start(0)

    GPIO.setup(R1, GPIO.OUT)
    a = GPIO.PWM(R1, 20)
    a.start(0)

    GPIO.setup(R2, GPIO.OUT)
    b = GPIO.PWM(R2, 20)
    b.start(0)


# cleanup(). Sets all motors off and sets GPIO to standard values
def cleanup():
    GPIO.cleanup()

def run():
	if GPIO.input(RUN_ON)==1 :		
		return True
		
	print "Will Not Run"
	return False	
	
# forward(speed): Sets both motors to move forward at speed. 0 <= speed <= 100
def forward(speed):
    p.ChangeDutyCycle(speed)
    q.ChangeDutyCycle(0)
    a.ChangeDutyCycle(speed)
    b.ChangeDutyCycle(0)
    p.ChangeFrequency(speed + 5)
    a.ChangeFrequency(speed + 5)	

#======================================================================
# UltraSonic Functions
#
# getDistance(). Returns the distance in cm to the nearest reflecting object. 0 == no object
def getDistance():
    GPIO.setup(sonar, GPIO.OUT)
    # Send 10us pulse to trigger
    GPIO.output(sonar, True)
    time.sleep(0.00001)
    GPIO.output(sonar, False)
    start = time.time()
    count=time.time()
    GPIO.setup(sonar,GPIO.IN)
    while GPIO.input(sonar)==0 and time.time()-count<0.1:
        start = time.time()
    count=time.time()
    stop=count
    while GPIO.input(sonar)==1 and time.time()-count<0.1:
        stop = time.time()
    # Calculate pulse length
    elapsed = stop-start
    # Distance pulse travelled in that time is time
    # multiplied by the speed of sound (cm/s)
    distance = elapsed * 34000
    # That was the distance there and back so halve the value
    distance = distance / 2
    return distance

# End of UltraSonic Functions    
#======================================================================
