import time
state = open("state.txt", "r+")
state.write("closed")
time.sleep(1)

try:
    while(True):
        print(str(state.read()))
        if state.read() == "closed":
            print("Opening")
            state.write("open")
            time.sleep(1)
        if state.read() == "open":
            print("Closing")
            state.write("closed")
            time.sleep(1)
        time.sleep(1)

except KeyboardInterrupt:
    state.close()
    exit()