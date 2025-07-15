#alaram clock
import datetime
import time
import os
import platform

def alarm_ring():
    print("⏰ WAKE UP!")
    
    if platform.system() == "Windows":
        os.system("echo \a")
    elif platform.system() == "Darwin":
        os.system("say 'Wake up!'")
    else:
        os.system("paplay /usr/share/sounds/freedesktop/stereo/complete.oga")

def alarm_clock():
    alarm_time = input("Set alarm time (HH:MM:SS): ")
    hour, minute, second = map(int, alarm_time.split(":"))

    while True:
        now = datetime.datetime.now()
        if now.hour == hour and now.minute == minute and now.second == second:
            alarm_ring()
            break
        time.sleep(1)

alarm_clock()
