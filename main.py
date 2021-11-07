import psutil
import time

temp = open("blacklist.txt")
programs = temp.read().splitlines()

print(programs)

while True:
    for program in psutil.process_iter():
        if program.name() in programs:
            program.kill()
            print(f"Killing {program.name()}")
    time.sleep(1)