import RPi.GPIO as GPIO          
from time import sleep

in1 = 11
in2 = 13
en = 15
temp1 = 1
in3 = 24
in4 = 23
en2 = 18  # Use a different GPIO channel for the second motor's enable pin
speed=50

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(en2, GPIO.OUT)  # Set up the second motor's enable pin
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
p = GPIO.PWM(en, 1000)
GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.LOW)
p2 = GPIO.PWM(en2, 1000)  # Set up the PWM object for the second motor

p.start(25)
p2.start(25)
print("\n")
print("The default speed & direction of the motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

def set_motor_speeds(left_speed, right_speed):
    p.ChangeDutyCycle(left_speed)
    p2.ChangeDutyCycle(right_speed)

def move_forward(speed):
    print("Moving forward")
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in1, GPIO.HIGH)

    GPIO.output(in4, GPIO.LOW)
    GPIO.output(in3, GPIO.HIGH)
    set_motor_speeds(speed, speed)

def move_backward(speed):
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)

    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)
    print("Moving backward")
    set_motor_speeds(speed, speed)

def turn_left(speed):
    print("Turning left")
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)

    GPIO.output(in4, GPIO.LOW)
    GPIO.output(in3, GPIO.HIGH)
    set_motor_speeds(0, speed)

def turn_right(speed):
    print("Turning right")
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in1, GPIO.HIGH)

    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    set_motor_speeds(speed,0)

def stop_movement():
    print("Stopping")
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)

    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    set_motor_speeds(0, 0)

while True:
    x = input()



    if x == 's':
        stop_movement()

    elif x == 'f':
        move_forward(speed)

    elif x == 'b':
        move_backward(speed)

    elif x == 'l':
        turn_left(speed)

    elif x == 'r':
        turn_right(speed)

    elif x == 'h':
        speed=100  # Set a higher speed (75%) for forward movement
    elif x=='m':
        speed=50
    elif x == 'e':
        GPIO.cleanup()
        print("GPIO Clean up")
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
