class Dieta():
    def __init__(self, nazwa: str, opis: str,
                 kalorie: int, cena: float) -> None:
        self._nazwa = nazwa
        self._opis = opis
        self._kalorie = kalorie
        self._cena = cena

    @property
    def nazwa(self):
        return self._nazwa

    @property
    def opis(self):
        return self._opis

    @property
    def kalorie(self):
        return self._kalorie

    @property
    def cena(self):
        return self._cena

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % vars(self)[item] for item in vars(self))
        )

    def __repr__(self) -> str:
        return self.__str__()
