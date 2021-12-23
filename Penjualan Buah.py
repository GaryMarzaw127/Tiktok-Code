
print('\n')

print('APLIKASI SEDERHANA PENJUALAN BUAH')

# harga buah perkilo
jeruk = 10000
salak = 13000
mangga = 15000
semangka = 8000

print('\n')
buah = int(input('MAU BELI BUAH APA ? \n1. Jeruk >> Rp.10.000\n2. Salak >> Rp.13.000\n3. Mangga >> Rp.15.000\n4. Semangka >> Rp.8000\n\nSilahkan Pilih : '))
print('\n')
berapa = int(input('Beli Berapa Kilo ? : '))

# kalkulasi
harga_jeruk = jeruk * berapa

harga_salak = salak * berapa

harga_mangga = mangga * berapa

harga_semangka = semangka * berapa

print('\n')
if buah == 1:
    print('====== ANDA MEMBELI BUAH JERUK ====== ')
    print('\n')
    print(f'jumlah harga : {jeruk} * {berapa} Kg = Rp. {harga_jeruk}')
    uang_anda = int(input('Uang Anda : Rp. '))
    kembalian_jeruk = uang_anda - harga_jeruk
    print(f'Kembalian : Rp. {kembalian_jeruk}')
elif buah == 2:
    print('====== ANDA MEMBELI BUAH SALAK ====== ')
    print('\n')
    print(f'jumlah harga : {salak} * {berapa} Kg = Rp. {harga_salak}')
    uang_anda = int(input('Uang Anda : Rp. '))
    kembalian_salak = uang_anda - harga_salak
    print(f'Kembalian : Rp. {kembalian_salak}')
elif buah == 3:
    print('====== ANDA MEMBELI BUAH MANGGA ====== ')
    print('\n')
    print(f'jumlah harga : {mangga} * {berapa} Kg = Rp. {harga_mangga}')
    uang_anda = int(input('Uang Anda : Rp. '))
    kembalian_mangga = uang_anda - harga_mangga
    print(f'Kembalian : Rp. {kembalian_mangga}')
elif buah == 4:
    print('====== ANDA MEMBELI BUAH SEMANGKA ====== ')
    print('\n')
    print(f'jumlah harga : {semangka} * {berapa} Kg = Rp. {harga_semangka}')
    uang_anda = int(input('Uang Anda : Rp. '))
    kembalian_semangka = uang_anda - harga_semangka
    print(f'Kembalian : Rp. {kembalian_semangka}')

print('\n')
