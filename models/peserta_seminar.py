from models.manusia import Manusia


class PesertaSeminar(Manusia):
    def bicara(self):
        print('My name is {}'.format(self.nama))
