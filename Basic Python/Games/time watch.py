import time
while True:
    localtime=time.localtime()
    a=time.strftime('%H:%M:%S %p:%A:%D ') #time watch
    print(a)
    time.sleep(1)

