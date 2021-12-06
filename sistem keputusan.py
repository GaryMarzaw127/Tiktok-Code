import random
import time

menu_makanan = [
    'bakso',
    'nasi padang',
    'mie goreng',
    'pecel lele',
    'nasi uduk',
    'nasi padang',
    'soto',
    'bakmi',
    'ayam goreng',
    'tahu genjrot',
    'bubur pedas',
    'pentol'
]

makanan = random.choice(menu_makanan)
print('suami : sayang... malam ini kita mau makan apa ya... ?')
print('istri : terserah deh ... ')
print('suami : oke ... (buat program sistem keputusan )')
print('\n')
print('loading...')
time.sleep(5)
print(f'jadi, yang kita makan malam ini adalah : ({makanan}) ')
