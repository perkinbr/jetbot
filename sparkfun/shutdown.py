# safe_shutdown_Pi.py
#
# -----------------------------------------------------------------------------
#                 Jetson  Safe Shutdown Python Script
# -----------------------------------------------------------------------------
# WRITTEN BY: Ho Yun "Bobby" Chan
# @ SparkFun Electronics
# DATE: 3/31/2020
# Updated on 1/20/2021 by Brian Perkins
# Now use wait_for_edge instead of spinning
# Work around bizarre Jetson GPIO behavior
# Based on code from the following blog and tutorials:
#
#    Kevin Godden
#    https://www.ridgesolutions.ie/index.php/2013/02/22/raspberry-pi-restart-shutdown-your-pi-from-python-code/
#
#    Pete Lewis
#    https://learn.sparkfun.com/tutorials/raspberry-pi-stand-alone-programmer#resources-and-going-further
#
#    Shawn Hymel
#    https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi/experiment-1-digital-input-and-output
#
# ==================== DESCRIPTION ====================
#
# This python script takes advantage of the Qwiic pHat v2.0's
# built-in general purpose button to safely reboot/shutdown you Pi:
#
#    1.) If you press the button momentarily, the Pi will shutdown.
#
# ========== TUTORIAL ==========
#  For more information on running this script on startup,
#  check out the associated tutorial to adjust your "rc.local" file:
#
#        https://learn.sparkfun.com/tutorials/raspberry-pi-safe-reboot-and-shutdown-button
#
# ========== PRODUCTS THAT USE THIS CODE ==========
#
#   Feel like supporting our work? Buy a board from SparkFun!
#
#        Qwiic pHAT v2.0
#        https://www.sparkfun.com/products/15945
#
#   You can also use any button but you would need to wire it up
#   instead of stacking the pHAT on your Pi.
#
# LICENSE: This code is released under the MIT License (http://opensource.org/licenses/MIT)
#
# Distributed as-is; no warranty is given
#
# -----------------------------------------------------------------------------

import time
import Jetson.GPIO as GPIO

# Pin definition
shutdown_pin = 11

# Suppress warnings
GPIO.setwarnings(False)

# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BOARD)

# Why do we need to do this? 
# My guess is the pullup on the PHat doesn't go quite high enough, but there's enough
# hysteresis in the level shifter that forcing it high keeps it there.


# modular function to shutdown Pi
def shut_down():
    print "shutting down"
    command = "/sbin/shutdown -h now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print output

# Check button if we want to shutdown the Pi safely
while True:
    # Yes, you need this insane rigamarole
    # For some reason when you use wait_for_edge you can't switch directions back to out
    # But everything works if you unexport the pin.  The easiest way to do this is that
    # I've found is to call cleanup

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(shutdown_pin, GPIO.IN)
    GPIO.cleanup()

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)


    # Why do this? Not sure.
    # Seems like the level shifter has some hystersis the pullup doesn't overcome
    # If we don't we can only get one edge
    GPIO.setup(shutdown_pin, GPIO.OUT)
    GPIO.output(shutdown_pin,1)

    GPIO.setup(shutdown_pin, GPIO.IN)

    # For troubleshooting, uncomment this line to output button status on command line
    #print GPIO.input(shutdown_pin)
    if GPIO.wait_for_edge(shutdown_pin, GPIO.FALLING):
        GPIO.input(shutdown_pin)
        shut_down()
        time.sleep(1)
