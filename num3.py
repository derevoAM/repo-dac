import RPi.GPIO as g
import time
dac = 22

g.setmode(g.BCM)
g.setup(22, g.OUT)
p = g.PWM(22, 1000)
p.start(0)
V = 3.3
try:
    while True:
        b = input("Enter a dutycycle ")
        if b.isdigit():
            a = int(b)
            if(a >= 0 and a <= 100):
                p.ChangeDutyCycle(a)
            else:
                print("Enter a dutycycle!!!")
                continue
        else:
            print("Enter a dutycycle!!!")
            continue
finally:
    p.stop()
    g.cleanup()
