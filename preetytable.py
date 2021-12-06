print('\n')
import time
print('TINGKATAN PADA START UP')
time.sleep(3)
from prettytable import PrettyTable

x = PrettyTable()
    
x.field_names = ["NO", "LEVEL", "NILAI VALUASI", "CONTOH"]
x.add_row(["1", 'COKROACH', '< 10 JUTA DOLLAR', 'STARTUP YANG BARU LAUNCHING'])
x.add_row(["2", 'PONIES', '> 10 JUTA DOLLAR', 'LINK AJA, AIRBNB'])
x.add_row(["3", 'CENTAURS', '> 100 JUTA DOLLAR', 'RUANG GURU, KREDIVO'])
x.add_row(["4", 'UNICORN', '> 1 MILLIAR DOLLAR', 'TOKOPEDIA'])
x.add_row(["5", 'DECACORN', '> 10 MILLIAR DOLLAR', 'GOJEK'])
x.add_row(["6", 'HECTOCORN', '> 100 MILLIAR DOLLAR', 'GOOGLE, APPLE, FACEBOOK'])

print(x)