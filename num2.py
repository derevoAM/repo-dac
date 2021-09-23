import RPi.GPIO as g
import time
dac = [26, 19, 13, 6, 5, 11, 9, 10]

g.setmode(g.BCM)
g.setup(dac, g.OUT, initial = g.LOW)

def dec2bin(a):
    return [int(i) for i in bin(a)[2:].zfill(8)]
def bin2dac(a):
    signal = dec2bin(a)
    g.output(dac, signal)
    return signal


i = 0
k = 0
try:
    while True:
#        a = input("Enter an integer number from 0 to 255 ")
#        if a.isdigit():
 #           str = int(a)
#            if(str > 255):
 #               print("Enter a number less than 256!!!")
  #              continue
        if i == 0:
          k = 1
        elif i == 255:
            k = -1 
        signal = bin2dac(i)
        i += k
        time.sleep(0.01)
 #       V = (str / 256) * 3.3
 #      else:
 #           print("Enter an integer number!!!")
 #           continue
finally:
    g.output(dac, g.LOW)
    g.cleanup()

