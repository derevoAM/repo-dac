import RPi.GPIO as g

dac = [26, 19, 13, 6, 5, 11, 9, 10]

def dec2bin(a):
    return [int(i) for i in bin(a)[2:].zfill(8)]
def bin2dac(a):
    signal = dec2bin(a)
    g.output(dac, signal)
    return signal

g.setmode(g.BCM)
g.setup(dac, g.OUT, initial = g.LOW)

try:
    while True:
        a = input("Enter an integer number from 0 to 255 ")
        if a.isdigit():
            str = int(a)
            if(str > 255):
                print("Enter a number less than 256!!!")
                continue
            signal = bin2dac(str)
            V = (str / 256) * 3.3
        else:
            print("Enter an integer number!!!")
            continue
finally:
    g.output(dac, g.LOW)
    g.cleanup()

