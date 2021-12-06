import random
import time

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "[]{()}*/-+,.;"

all = lower + upper + number + symbol
length = 16
password = "".join(random.sample(all, length))
print('\n')
print('>'*50)
print('\n')
print('LOADING.....')
time.sleep(2)
print('\n')
print(f'HASIL PASSWORDNYA: {password}')
print('\n')
print('>'*50)
print('\n')
