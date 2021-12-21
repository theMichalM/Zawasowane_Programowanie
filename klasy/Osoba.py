class Osoba:

    def __init__(self, imie: str, nazwisko: str, nr_tel: str) -> None:
        self._imie = imie
        self._nazwisko = nazwisko
        self._nr_tel = nr_tel

    @property
    def imie(self):
        return self._imie

    @property
    def nazwisko(self):
        return self._nazwisko

    @property
    def nr_tel(self):
        return self._nr_tel

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % vars(self)[item] for item in vars(self))
        )
