import RPi.GPIO as GPIO
import time

# make the GPIO pins ready
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# ready the output pins
valveIndicator = 4
GPIO.setup(valveIndicator, GPIO.OUT)

# turn on the valve
GPIO.output(valveIndicator, 1)
time.sleep(5)
GPIO.output(valveIndicator, 0)

# cleanup the GPIO usage
GPIO.cleanup()
