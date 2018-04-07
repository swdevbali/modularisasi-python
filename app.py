title = 'Penampilan Data Peserta Seminar'
print(title)

#encapsulation
# PEP - 8
class Manusia:
    def __init__(self):
        self.nama = 'Unnamed'
        self.usia = 25
        self.alamat = 'Jogja'

    def bicara(self):
        print('Hoi! Nama saya {}'.format(self.nama))

    def __repr__(self):
        """
        Dipanggil saat object di cetak oleh print
        :return:
        """
        return 'Nama {}, usia {}, alamat {}'.format(
            self.nama, self.usia, self.alamat)

class PesertaSeminar(Manusia):
    def bicara(self):
        print('My name is {}'.format(self.nama))


#instantiation
adam = Manusia()
adam.nama = 'Adam'


fulan = PesertaSeminar()
fulanah = PesertaSeminar()

fulanah.nama = 'Susi'
fulanah.usia = 28
fulanah.alamat = 'Bali'


fulan.nama = 'Joko'
fulan.usia = 53
fulan.alamat = 'Solo'

# polymorphism
adam.bicara()
fulan.bicara()
fulanah.bicara()