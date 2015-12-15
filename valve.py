#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import sys

# define the GPIO pin mapping
mapping = ["void", 18, 23, 24, 25]

# make the GPIO pins ready
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

print "Opening valve " + sys.argv[1] + " for " + sys.argv[2] + " seconds"

# ready the output pins
valveIndicator = mapping[int(sys.argv[1])]
GPIO.setup(valveIndicator, GPIO.OUT)

# turn on the valve
GPIO.output(valveIndicator, 1)
time.sleep(float(sys.argv[2]))
GPIO.output(valveIndicator, 0)

print "Closing valve " + sys.argv[1]

# cleanup the GPIO usage
GPIO.cleanup()
