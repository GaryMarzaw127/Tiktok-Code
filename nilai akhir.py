print('\n')
print('APLIKASI PENGHITUNG NILAI UJIAN AKHIR')
print('\n')

kehadiran = int(input('Masukkan Nilai Kehadiran : '))
tgs = int(input('Masukkan Nilai Tugas : '))
uts = int(input('Masukkan Nilai UTS : '))
uas = int(input('Masukkan Nilai UAS : '))

nilai_kehadiran = kehadiran * 0.1
nilai_tgs = tgs * 0.2
nilai_uts = uts * 0.3
nilai_uas = uas * 0.4

print('\n')
nilai_akhir = nilai_kehadiran + nilai_tgs + nilai_uts + nilai_uas
print(f"Nilai Akhir : {nilai_akhir}")

print('\n')

if nilai_akhir >= 80:
    print('Keterangan : A ')
elif nilai_akhir >= 70:
    print('Keterangan : B ')
elif nilai_akhir >= 60:
    print('Keterangan : C ')
elif nilai_akhir >= 50:
    print('Keterangan : D ')
else:
    print('Keterangan : E ')
print('\n')