import os

def servo_init():
	cmd0 = "echo 0=0 > /dev/servoblaster"
	cmd1 = "echo 1=0 > /dev/servoblaster"	
	os.system(cmd0)
	os.system(cmd1)


def servo_forward():
	# full speed ahead
	cmd0 = "echo 0=250 > /dev/servoblaster"
	cmd1 = "echo 1=-250 > /dev/servoblaster"
	os.system(cmd0)
	os.system(cmd1)
	

def servo_backward():
	# slow reverse back
	cmd0 = "echo 0=-200 > /dev/servoblaster"
	cmd1 = "echo 1=200 > /dev/servoblaster"
	os.system(cmd0)
	os.system(cmd1)
	
def servo_right():		
	cmd0 = "echo 0=200 > /dev/servoblaster"
	cmd1 = "echo 1=200 > /dev/servoblaster"
	os.system(cmd0)
	os.system(cmd1)
	
def servo_left():		
	cmd0 = "echo 0=-200 > /dev/servoblaster"	
	cmd1 = "echo 1=-200 > /dev/servoblaster"
	os.system(cmd0)
	os.system(cmd1)
	
def servo_stop():		
	cmd0 = "echo 0=0 > /dev/servoblaster"
	cmd1 = "echo 1=0 > /dev/servoblaster"	
	os.system(cmd0)
	os.system(cmd1)
	
def servo_cleanup():
	servo_stop()
