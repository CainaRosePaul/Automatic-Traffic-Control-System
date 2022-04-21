from right_side import right
from left_side import left


import serial

import time

serialcomm = serial.Serial('COM4', 9600)

serialcomm.timeout = 1
i= input("Enter Input: ").strip()
serialcomm.write("rrlron".encode())

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
flagr=0
flagl=0
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
            i = input("Enter Input: ").strip()
            serialcomm.write("lroff".encode())

            sleep(timer)
            i = input("Enter Input: ").strip()
            serialcomm.write("lgoff".encode())
            test()
        timer=45+(3*(rc-1))
        print("green @ right")
        i = input("Enter Input: ").strip()
        serialcomm.write("rroff".encode())
        sleep(timer)
        i = input("Enter Input: ").strip()
        serialcomm.write("rgoff".encode())
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
            i = input("Enter Input: ").strip()
            serialcomm.write("rroff".encode())
            sleep(timer)
            i = input("Enter Input: ").strip()
            serialcomm.write("rgoff".encode())
            # sleep(timer)
            test()
        timer =45+(3*(lc-1))
        print("green @ left")
        i = input("Enter Input: ").strip()
        serialcomm.write("lroff".encode())

        sleep(timer)
        i = input("Enter Input: ").strip()
        serialcomm.write("lgoff".encode())
        # sleep(timer)
        test()
    else:
        if(current==1):
            current = 0
            flagl=flagl+1
            flagr=0
            timer=45+(3*(lc-1))
            print("green @ left")
            i = input("Enter Input: ").strip()
            serialcomm.write("lroff".encode())

            sleep(timer)
            i = input("Enter Input: ").strip()
            serialcomm.write("lgoff".encode())
            # sleep(timer)
            test()
        else:
            current = 1
            flagr=flagr+1
            flagl = 0
            timer = 45 + (3 * (rc - 1))
            print("green @ right")
            i = input("Enter Input: ").strip()
            serialcomm.write("rroff".encode())
            sleep(timer)
            i = input("Enter Input: ").strip()
            serialcomm.write("rgoff".encode())
            # sleep(timer)
            test()

test()









