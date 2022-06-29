from datetime import datetime
from playsound import playsound

# userinput = input('enter the time of alarm: HH:MM::SS \n')
userinput = '06:17:00'

alarm_hour = userinput[0:2]
alarm_minute = userinput[3:5]
alarm_second = userinput[6:8]
print('setting up an alarm')

while True:
    current_time = datetime.now()

    current_hour = current_time.strftime("%I")
    current_minute = current_time.strftime("%M")
    current_second = current_time.strftime("%S")

    if alarm_hour == current_hour:
        if alarm_minute == current_minute:
            if alarm_second == current_second:
                print('wake up')
                playsound("alarm.mp3")
                break
