import readchar
import time

lastTime = time.time() + 10000000

print("<spTimer>")
while True:
    kb = readchar.readchar()
    if kb == ' ':
        interval = time.time() - lastTime
        if interval > 1:
            print("\nTime : " + str('{:.2f}'.format(interval)))
            lastTime = time.time() + 10000000
        else:
            print("\rReady", end="")
            lastTime = time.time()
    if kb == 'q':
        print("Bye")
        break


