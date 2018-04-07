from models.manusia import Manusia
from models.peserta_seminar import PesertaSeminar

title = 'Penampilan Data Peserta Seminar'
print(title)

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