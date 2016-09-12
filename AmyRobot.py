import RPi.GPIO as GPIO
import time
import initio
import lcd
import servo

try:
	initio.init()
	lcd.lcd_init()	
	servo.servo_init()
	lcd.lcd_clear()
	while initio.run():	
		servo.servo_forward()
		dist = int(initio.getDistance())
		msg = "Distance = " + str(dist)		
		lcd.lcd_line2(msg,2)	
		if dist < 8 : 
			initio.forward(5)
			lcd.lcd_line2("Eeeeek!",2)
			servo.servo_backward()
			time.sleep(1)
			servo.servo_right()
			time.sleep(1)
			servo.servo_stop()
		else :
		    initio.forward(100)
			 
		time.sleep(0.01)

except KeyboardInterrupt:
    print
    pass

finally:	
	servo.servo_cleanup()
	lcd.lcd_clear()
	lcd.lcd_line1("Goodbye!",2)
	lcd.lcd_cleanup()   
	initio.cleanup()
