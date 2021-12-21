from klasy.Osoba import Osoba


class Dietetyk(Osoba):

    def __init__(self, imie: str, nazwisko: str,
                 nr_tel: str, data_zatrudnienia: str) -> None:
        super().__init__(imie, nazwisko, nr_tel)
        self._data_zatrudnienia = data_zatrudnienia

    @property
    def data_zatrudnienia(self):
        return self._data_zatrudnienia

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % vars(self)[item] for item in vars(self))
        )
