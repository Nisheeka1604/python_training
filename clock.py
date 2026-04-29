import time
import sys
h=3
m=42
s=0
print("\033[1;32mClock\033[0m")
while True:
    sys.stdout.write("\r{:02d}:{:02d}:{:02d}".format(h, m, s))
    sys.stdout.flush()
    time.sleep(1)
    s = s + 1
    if s == 60:
        s = 0
        m = m + 1
    if m == 60:
        m = 0
        h = h + 1
    if h == 13:
        h = 1
        m = 0
        s = 0
print()