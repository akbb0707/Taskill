import psutil
import time
import signal

def handler(signum, frame):
    print('What are you, mentally weak?')

signal.signal(signal.SIGINT, handler)

temp = open("blacklist.txt")
programs = temp.read().splitlines()

print(programs)

while True:
    for program in psutil.process_iter():
        if program.name() in programs:
            program.kill()
            print(f"Killing {program.name()}")
    time.sleep(1)