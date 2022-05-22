from right_side import right
from left_side import left


import serial

import time

arduino1 = serial.Serial('COM5', 9000)
arduino2 = serial.Serial('COM3', 9600)
time.sleep(1)

arduino1.write(b'1')

#rc = right()
#lc = left()

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
            arduino1.write(b'2')

            sleep(timer-3)

            arduino1.write(b'6')

            sleep(3)

            arduino2.write(b'1')
            data1 = arduino2.readline()
            str = data1.decode('utf-8')
            count1 = int(float(str))
            print(count1)

            data2 = arduino2.readline()
            str = data2.decode('utf-8')
            count2 = int(float(str))
            print(count2)

            if (count1 - count2 == 0):
                print("No Vehicle on the bridge")
                arduino2.write(b'2')
            else:
                print("Vehicle is there on the bridge")
                while(count1 != count2):
                    print("Vehicle is still there")
                    arduino2.write(b'1')
                    data1 = arduino2.readline()
                    str = data1.decode('utf-8')
                    count1 = int(float(str))


                    data2 = arduino2.readline()
                    str = data2.decode('utf-8')
                    count2 = int(float(str))

                print("bridge is clear")
                arduino2.write(b'2')
            arduino1.write(b'3')
            test()
        timer=45+(3*(rc-1))
        print("green @ right")

        arduino1.write(b'4')

        sleep(timer-3)

        arduino1.write(b'7')

        sleep(3)

        arduino2.write(b'1')
        data1 = arduino2.readline()
        str = data1.decode('utf-8')
        count1 = int(float(str))
        print(count1)

        data2 = arduino2.readline()
        str = data2.decode('utf-8')
        count2 = int(float(str))
        print(count2)

        if (count1 - count2 == 0):
            print("No Vehicle on the bridge")
            arduino2.write(b'2')
        else:
            print("Vehicle is there on the bridge")
            while (count1 != count2):
                print("Vehicle is still there")
                arduino2.write(b'1')
                data1 = arduino2.readline()
                str = data1.decode('utf-8')
                count1 = int(float(str))

                data2 = arduino2.readline()
                str = data2.decode('utf-8')
                count2 = int(float(str))
            print("Bridge is clear")
            arduino2.write(b'2')

        arduino1.write(b'5')

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

            arduino1.write(b'4')

            sleep(timer-3)

            arduino1.write(b'7')

            sleep(3)

            arduino2.write(b'1')
            data1 = arduino2.readline()
            str = data1.decode('utf-8')
            count1 = int(float(str))
            print(count1)

            data2 = arduino2.readline()
            str = data2.decode('utf-8')
            count2 = int(float(str))
            print(count2)

            if (count1 - count2 == 0):
                print("No Vehicle on the bridge")
                arduino2.write(b'2')
            else:
                print("Vehicle is there on the bridge")
                while (count1 != count2):
                    print("Vehicle is still there")
                    arduino2.write(b'1')
                    data1 = arduino2.readline()
                    str = data1.decode('utf-8')
                    count1 = int(float(str))

                    data2 = arduino2.readline()
                    str = data2.decode('utf-8')
                    count2 = int(float(str))
                print("Bridge is clear")
                arduino2.write(b'2')

            arduino1.write(b'5')

            # sleep(timer)
            test()
        timer =45+(3*(lc-1))
        print("green @ left")

        arduino1.write(b'2')

        sleep(timer-3)

        arduino1.write(b'6')

        sleep(3)

        arduino2.write(b'1')
        data1 = arduino2.readline()
        str = data1.decode('utf-8')
        count1 = int(float(str))
        print(count1)

        data2 = arduino2.readline()
        str = data2.decode('utf-8')
        count2 = int(float(str))
        print(count2)

        if (count1 - count2 == 0):
            print("No Vehicle on the bridge")
            arduino2.write(b'2')
        else:
            print("Vehicle is there on the bridge")
            while (count1 != count2):
                print("Vehicle is still there")
                arduino2.write(b'1')
                data1 = arduino2.readline()
                str = data1.decode('utf-8')
                count1 = int(float(str))

                data2 = arduino2.readline()
                str = data2.decode('utf-8')
                count2 = int(float(str))
            print("Bridge is clear")
            arduino2.write(b'2')

        arduino1.write(b'3')
        # sleep(timer)
        test()
    else:
        if(current==1):
            current = 0
            flagl=flagl+1
            flagr=0
            timer=45+(3*(lc-1))
            print("green @ left")

            arduino1.write(b'2')

            sleep(timer-3)

            arduino1.write(b'6')

            sleep(3)

            arduino2.write(b'1')
            data1 = arduino2.readline()
            str = data1.decode('utf-8')
            count1 = int(float(str))
            print(count1)

            data2 = arduino2.readline()
            str = data2.decode('utf-8')
            count2 = int(float(str))
            print(count2)

            if (count1 - count2 == 0):
                print("No Vehicle on the bridge")
                arduino2.write(b'2')
            else:
                print("Vehicle is there on the bridge")
                while (count1 != count2):
                    print("Vehicle is still there")
                    arduino2.write(b'1')
                    data1 = arduino2.readline()
                    str = data1.decode('utf-8')
                    count1 = int(float(str))

                    data2 = arduino2.readline()
                    str = data2.decode('utf-8')
                    count2 = int(float(str))
                print("Bridge is clear")
                arduino2.write(b'2')

            arduino1.write(b'3')
            test()
        else:
            current = 1
            flagr=flagr+1
            flagl = 0
            timer = 45 + (3 * (rc - 1))
            print("green @ right")

            arduino1.write(b'4')
            sleep(timer-3)

            arduino1.write(b'7')

            sleep(3)

            arduino2.write(b'1')
            data1 = arduino2.readline()
            str = data1.decode('utf-8')
            count1 = int(float(str))
            print(count1)

            data2 = arduino2.readline()
            str = data2.decode('utf-8')
            count2 = int(float(str))
            print(count2)

            if (count1 - count2 == 0):
                print("No Vehicle on the bridge")
                arduino2.write(b'2')
            else:
                print("Vehicle is there on the bridge")
                while (count1 != count2):
                    print("Vehicle is still there")
                    arduino2.write(b'1')
                    data1 = arduino2.readline()
                    str = data1.decode('utf-8')
                    count1 = int(float(str))

                    data2 = arduino2.readline()
                    str = data2.decode('utf-8')
                    count2 = int(float(str))
                print("Bridge is clear")
                arduino2.write(b'2')

            arduino1.write(b'5')
            # sleep(timer)
            test()

test()