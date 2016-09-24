# Load library functions we want
import time
import os
import sys
import pygame

# Settings for the joystick
axisUpDown = 1                          # Joystick axis to read for up / down position
axisUpDownInverted = False              # Set this to True if up and down appear to be swapped
axisLeftRight = 2                       # Joystick axis to read for left / right position
axisLeftRightInverted = False           # Set this to True if left and right appear to be swapped
buttonResetEpo = 9                      # Joystick button number to perform an EPO reset (Start)
buttonSlow = 6                          # Joystick button number for driving slowly whilst held (L2)
slowFactor = 0.5                        # Speed to slow to when the drive slowly button is held, e.g. 0.5 would be half speed
buttonFastTurn = 7                      # Joystick button number for turning fast (R2)
interval = 0.00                         # Time between updates in seconds, smaller responds faster but uses more processor time

pygame.init()
#pygame.display.set_mode((1,1))
print 'Waiting for joystick... (press CTRL+C to abort)'
while True:
    try:
        try:
            pygame.joystick.init()
            # Attempt to setup the joystick
            if pygame.joystick.get_count() < 1:
                # No joystick attached, toggle the LED
                print('No Joystick attached')
                pygame.joystick.quit()
                time.sleep(0.5)
            else:
                # We have a joystick, attempt to initialise it!
                joystick = pygame.joystick.Joystick(0)
                break
        except pygame.error:
            # Failed to connect to the joystick, toggle the LED
            print('Failled to connect to joystick')
            pygame.joystick.quit()
            time.sleep(0.5)
    except KeyboardInterrupt:
        # CTRL+C exit, give up
        print '\nUser aborted'

        sys.exit()
print 'Joystick found'
joystick.init()

try:
    print 'Press CTRL+C to quit'
    running = True    
    upDown = 0.0
    leftRight = 0.0
    # Loop indefinitely
    while running:
        # Get the latest events from the system
        hadEvent = False
        events = pygame.event.get()
        # Handle each event individually
        for event in events:
            if event.type == pygame.JOYAXISMOTION:
                upDown = joystick.get_axis(axisUpDown)
                leftRight = joystick.get_axis(axisLeftRight)
                if leftRight != 0:
                    print('left ', leftRight)
                if upDown != 0:
                    print('up ',upDown)
                
            # Check for button presses
            if event.type == pygame.JOYBUTTONDOWN:
                if joystick.get_button(buttonResetEpo):
                    print('reset')
                    running = False
        
        # Wait for the interval period
        time.sleep(interval)
        
except KeyboardInterrupt:
    # CTRL+C exit, disable all drives
    print ('Ctrl-C')
    
print ('Done')
