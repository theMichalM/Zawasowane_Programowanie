from klasy.Diata import Dieta
from klasy.Osoba import Osoba


class Zamowienie:

    _nr_zamowienia: int
    _data: str
    _diety: list[Dieta]
    _pacjent: Osoba
    _dietetyk: Osoba

    def __init__(self) -> None:
        pass

    @property
    def nr_zamowienia(self):
        return self._nr_zamowienia

    @nr_zamowienia.setter
    def nr_zamowienia(self, nr_zamowienia: int):
        self._nr_zamowienia = nr_zamowienia

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data: str):
        self._data = data

    @property
    def diety(self):
        return self._diety

    @diety.setter
    def diety(self, diety: list[Dieta]):
        self._diety = diety

    @property
    def pacjent(self):
        return self._pacjent

    @pacjent.setter
    def pacjent(self, pacjent: Osoba):
        self._pacjent = pacjent

    @property
    def dietetyk(self):
        return self._dietetyk

    @dietetyk.setter
    def dietetyk(self, dietetyk: Osoba):
        self._dietetyk = dietetyk

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % vars(self)[item] for item in vars(self))
        )

    def get_cena(self):
        cena: float = 0
        for d in self.diety:
            cena += d.cena
        return round(cena, 2)

    def get_kal(self):
        kal: int = 0
        for d in self.diety:
            kal += d.kalorie
        return kal
