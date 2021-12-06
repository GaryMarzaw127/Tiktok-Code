class aku:
    def suka_rebahan(self,kesukaan):
        self.kesukaan = kesukaan

class kamu:
    def suka_jalan_jalan(self, kesukaan):
        self.kesukaan = kesukaan

class anak_kita(aku, kamu):
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

print('KESUKAAN AKU : SUKA REBAHAN')
print('KESUKAAN KAMU : SUKA JALAN-JALAN')
print('KETIKA KESUKAAN AKU + KESUKAAN KAMU = KESUKAAN ANAK KITA')
print('\n')
print('ANAK KITA')

anak_kita1 = anak_kita('Jasmine', 2)
anak_kita1.suka_rebahan('suka rebahan')
anak_kita1.suka_jalan_jalan('suka jalan-jalan')

print(anak_kita1.__dict__)



