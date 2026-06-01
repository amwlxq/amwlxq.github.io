import time
ms = 0
s = 0
m = 0
h = 0
while True:
    ms += 1
    if ms == 1000:
        s += 1
        ms = 0
    if s == 60:
        m += 1
        s = 0
    if m == 60:
        h += 1
        m = 0
    if ms < 10:
        print(f'{h}:{m}:{s}.00{ms}')
    if ms < 100 and ms > 9:
        print(f'{h}:{m}:{s}.0{ms}')
    if ms<1000 and ms>99:
        print(f'{h}:{m}:{s}.{ms}')
    time.sleep(0.001)
