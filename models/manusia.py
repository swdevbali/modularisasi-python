#encapsulation
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