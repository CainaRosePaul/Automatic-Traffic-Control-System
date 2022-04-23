from right_side import right
from left_side import left


import serial

import time

arduino = serial.Serial('COM3', 9600)
time.sleep(1)

arduino.write(b'1')

#rc = right()
#lc = left()

import time
def sleep(seconds):
    print(f"sleeping for {seconds}")
    time.sleep(seconds)
    print("done")
#rc=3
#lc=2
current=1
flagr = 0
flagl = 0

def test():
    global current
    global flagr
    global flagl


    rc = right()
    lc = left()
    if(rc>lc):
        current=1
        flagr=flagr+1
        flagl=0
        if(flagr==3 or (flagr==2 and rc-lc<=2)):
            current=0
            flagl=flagl+1
            flagr=0
            timer=45+(3*(lc-1))
            print("green @ left")
            arduino.write(b'2')

            sleep(timer)

            arduino.write(b'3')
            test()
        timer=45+(3*(rc-1))
        print("green @ right")

        arduino.write(b'4')

        sleep(timer)

        arduino.write(b'5')

        test()
    elif(lc>rc):
        current=0
        flagl=flagl+1
        flagr=0
        if (flagl==3 or (flagl==2 and lc-rc <= 2)):
            current=1
            flagr=flagr+1
            flagl=0
            timer=45+(3*(rc-1))
            print("green @ right")

            arduino.write(b'4')

            sleep(timer)

            arduino.write(b'5')

            # sleep(timer)
            test()
        timer =45+(3*(lc-1))
        print("green @ left")

        arduino.write(b'2')

        sleep(timer)

        arduino.write(b'3')
        # sleep(timer)
        test()
    else:
        if(current==1):
            current = 0
            flagl=flagl+1
            flagr=0
            timer=45+(3*(lc-1))
            print("green @ left")

            arduino.write(b'2')

            sleep(timer)

            arduino.write(b'3')
            test()
        else:
            current = 1
            flagr=flagr+1
            flagl = 0
            timer = 45 + (3 * (rc - 1))
            print("green @ right")

            arduino.write(b'4')
            sleep(timer)
            arduino.write(b'5')
            # sleep(timer)
            test()

test()