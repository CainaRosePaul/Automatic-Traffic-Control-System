import time
def sleep(seconds):
    print(f"sleeping for {seconds}")
    time.sleep(seconds)
    print("done")
rc=3
lc=2
#while(true):

flagr=0
flagl=0
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
        sleep(timer)
    timer=45+(3*(rc-1))
    print("green @ right")
    sleep(timer)
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
        sleep(timer)
    timer =45+(3*(lc-1))
    print("green @ left")
    sleep(timer)
else:
    if(current==1):
        current = 0
        flagl=flagl+1
        flagr=0
        timer=45+(3*(lc-1))
        print("green @ left")
    else:
        current = 1
        flagr=flagr+1
        flagl = 0
        timer = 45 + (3 * (rc - 1))
        print("green @ right")







