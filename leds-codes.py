import RPi.GPIO as GPIO
import time

RED = 17
YELLOW = 27
GREEN = 22

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)

#print("LEDs on")
#GPIO.output(RED, GPIO.HIGH)
#GPIO.output(YELLOW, GPIO.HIGH)
#GPIO.output(GREEN, GPIO.HIGH)
#time.sleep(2)
#print("LEDs off")
#GPIO.output(RED, GPIO.LOW)
#GPIO.output(YELLOW, GPIO.LOW)
#GPIO.output(GREEN, GPIO.LOW)

def flash_on_green():
    print("LED GREEN is ON")
    GPIO.output(GREEN, GPIO.HIGH)
    
def flash_off_green():
    print("LED GREEN is OFF")
    GPIO.output(GREEN, GPIO.LOW)
    
def flash_on_yellow():
    print("LED YELLOW is ON")
    GPIO.output(YELLOW, GPIO.HIGH)
    
def flash_off_yellow():
    print("LED YELLOW is OFF")
    GPIO.output(YELLOW, GPIO.LOW)
    
def flash_on_red():
    print("LED RED is ON")
    GPIO.output(RED, GPIO.HIGH)
    
def flash_off_red():
    print("LED RED is OFF")
    GPIO.output(RED, GPIO.LOW)
    