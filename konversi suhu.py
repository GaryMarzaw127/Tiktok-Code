print('\n')

print('APLIKASI SEDERHANA KONVERSI SUHU')
print('\n')
celcius = int(input('Masukkan Suhu Celcius : '))

fahrenheit = (9/5*celcius) + 32
reamur = 4/5 * celcius
kelvin = 273 + celcius
rankine = (9/5 * celcius) + 491.67
delisle = (100 - celcius) * 3/2
romer = (21/40 * celcius) + 7.5
newton = 0.33 * celcius

print('\n')
print('='*5, 'HASIL KONVERSI', '='*5)
print(f' fahrenheit: {fahrenheit}\n reamur: {reamur}\n kelvin: {kelvin}\n rankine: {rankine} \
    \n delisle: {delisle}\n romer: {romer}\n newton: {newton}')
print('\n')













