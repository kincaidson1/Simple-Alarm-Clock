# This imported librarys helps the alarm to function accordingly

import datetime
import time
from playsound import playsound

# This def function sets the alarm for the given hour and minute.
def set_alarm(hour, minute):
  
# This segment requires User input

  am_or_pm = input("AM or PM: ").lower()
  
# This section deals with adding 12 to the hour value for PM time, if it isn't already 12.
  if am_or_pm == 'pm' and hour != 12:
    hour += 12
    
# This section deals with seting the hour value for AM time to 0 if it is 12 already.   
  elif am_or_pm == 'am' and hour == 12:
    hour = 0

# This section is the Alarm Loop

  while True:
    current_time = datetime.datetime.now()

    if current_time.hour == hour and current_time.minute == minute:
      print('Alarm ringing........')
      playsound("Alarm2.mp3")  
      print('Alarm stopped')
      break  
    else:
      time.sleep(1)  
      

# The require the hour and minute from the user

hour = int(input("Set the hour: "))
minute = int(input("Set the minute: "))

set_alarm(hour, minute)
