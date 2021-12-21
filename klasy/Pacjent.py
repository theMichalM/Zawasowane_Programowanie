from klasy.Osoba import Osoba


class Pacjent(Osoba):

    def __init__(self, imie: str, nazwisko: str,
                 nr_tel: str, adres: str) -> None:
        super().__init__(imie, nazwisko, nr_tel)
        self._adres = adres

    @property
    def adres(self):
        return self._adres

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % vars(self)[item] for item in vars(self))
        )
