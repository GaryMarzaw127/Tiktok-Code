print('\n')
print('KALKULATOR SEDERHANA MENGGUNAKAN BAHASA PYTHON')
print('\n')

angka1 = int(input('Masukkan Angka 1 : '))
angka2 = int(input('Masukkan Angka 2 : '))

print('\n')
print('Pilihan Operasi:\n1. Tambah\n2. Kurang\n3. Kali\n4. Bagi\n5. Pangkat\n6. Semua Operasi\n')
print('\n')

pilihan = int(input('Masukkan Pilihan Operasi : '))

# Tambah
tambah = angka1 + angka2
tambah1 = (f'Jumlah >> Tambah : {angka1} + {angka2} = {tambah}')

# Kurang
kurang = angka1 - angka2
kurang1 = (f'Jumlah >> Kurang : {angka1} - {angka2} = {kurang}')

# Kali
kali = angka1 * angka2
kali1 = (f'Jumlah >> Kali : {angka1} * {angka2} = {kali}')

# Bagi
bagi = angka1 / angka2
bagi1 = (f'Jumlah >> Bagi :  {angka1} / {angka2} = {bagi}')

# Pangkat
pangkat = angka1 ** angka2
pangkat1 = (f'Jumlah >> Pangkat : {angka1} pangkat {angka2} = {pangkat}')



if pilihan == 1:
    print('\n')
    print(tambah1)
elif pilihan == 2:
    print('\n')
    print(kurang1)
elif pilihan == 3:
    print('\n')
    print(kali1)
elif pilihan == 4:
    print('\n')
    print(bagi1)
elif pilihan == 5:
    print('\n')
    print(pangkat1)
elif pilihan == 6:
    print('\n')
    print(tambah1)
    print(kurang1)
    print(kali1)
    print(bagi1)
    print(pangkat1)  
else:
    print('pilihan tidak tersedia')
print('\n')