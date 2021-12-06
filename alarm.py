
import datetime
from playsound import playsound
print('\n')
alarm_hour = int(input('masukkan jam: '))
print('\n')
alarm_min = int(input('masukkan min : '))
print('\n')
alarm_am = input('am/pm : ')
print('\n')

if alarm_am == 'pm':
    alarm_hour += 12

while True:
    if alarm_hour == datetime.datetime.now().hour and alarm_min == datetime.datetime.now().minute:
        print('playing music ....')
        playsound('music.mp3')
        break
                 
