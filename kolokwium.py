class Produkt:
    def __init__(self, numer_seryjny: int, nazwa: str, data_produkcji: str, waga: str, cena: float) -> None:
        self._numer_seryjny = numer_seryjny
        self._nazwa = nazwa
        self._data_produkcji = data_produkcji
        self._waga = waga
        self._cena = cena

    def get_numer_seryjny(self):
        return self._numer_seryjny

    def get_nazwa(self):
        return self._nazwa

    def get_numer_seryjny(self):
        return self._numer_seryjny

    def get_data_produkcji(self):
        return self._data_produkcji

    def get_waga(self):
        return self._waga

    def get_cena(self):
        return self._cena

    def __str__(self) -> str:
        return f'Nazwa: {self._nazwa}, numer seryjny: {self._numer_seryjny}, data produkcji: {self._data_produkcji}, waga: {self._waga}, cena: {self._cena}'


class Magazyn:
    def __init__(self, miasto: str, adres: str, produkty: list, wolne_miejsce: str, pracownicy: int) -> None:
        self._miasto = miasto
        self._adres = adres
        self._produkty = produkty
        self._wolne_miejsce = wolne_miejsce
        self._pracownicy = pracownicy

    def get_miasto(self):
        return self._miasto

    def get_adres(self):
        return self._adres

    def get_produkty(self):
        return self._produkty

    def get_wolne_miejsce(self):
        return self._wolne_miejsce

    def get_pracownicy(self):
        return self._pracownicy

    def __str__(self) -> str:
        produktystr: str = ''
        for p in self._produkty:
            produktystr += str(p)+'\n'
        return f'Miasto: {self._miasto}, adres: {self._adres}, produkty:\n{produktystr}, wolne miejsce w magazynie: {self._wolne_miejsce}, ilość pracowników magazynu: {self._pracownicy}'


class KlientDetaliczny:
    def __init__(self,id: int, imie: str, nazwisko: str, adres: str, numer_telefony: int) -> None:
        self._id = id
        self._imie = imie
        self._nazwisko = nazwisko
        self._adres = adres
        self._numer_telefonu = numer_telefony

    def get_id(self):
        return self._id

    def get_imie(self):
        return self._imie

    def get_nazwisko(self):
        return self._nazwisko

    def get_adres(self):
        return self._adres

    def get_numer_telefonu(self):
        return self._numer_telefonu

    def __str__(self) -> str:
        return f'{self._imie} {self._nazwisko}, Id: {str(self._id)}, adres: {self._adres}, numer telefonu: {str(self._numer_telefonu)}'


class Zamowienie:
    def __init__(self) -> None:
        self._nr_zamowienia: int = 0
        self._klient: KlientDetaliczny = ''
        self._produkty:list = []
        self._data_zamowienia: str = ''
        self._stan: str = ''

    def get_nr_zamowienia(self):
        return self._nr_zamowienia

    def set_nr_zamowienia(self, nr_zamowienia):
        self._nr_zamowienia = nr_zamowienia

    def get_klient(self):
        return self._klient

    def set_klient(self, klient):
        self._klient = klient

    def get_produkty(self):
        return self._produkty

    def set_produkty(self, produkty):
        self._produkty = produkty

    def get_data_zamowienia(self):
        return self._data_zamowienia

    def set_data_zamowienia(self, data_zamowienia):
        self._data_zamowienia = data_zamowienia

    def get_stan(self):
        return self._stan

    def set_stan(self, stan):
        self._stan = stan

    def get_cena(self) -> float:
        cena: float = 0
        for p in self._produkty:
            cena += p
        return round(cena,2)

    def get_adres(self) -> str:
        return self._klient.get_adres

    def __str__(self) -> str:
        produktystr: str = ''
        for p in self._produkty:
            produktystr += str(p)+'\n'
        return f'klient: {str(self._klient)},produkty:\n{produktystr}'


class KlientBiznesowy(KlientDetaliczny):
    def __init__(self, id: int, imie: str, nazwisko: str, adres: str, numer_telefony: int, firma: str) -> None:
        super().__init__(id, imie, nazwisko, adres, numer_telefony)
        self._firma = firma

    def get_firma(self):
        return self._firma

    def __str__(self) -> str:
        return str(super) + f', firma: {self._firma}'


k1 = KlientDetaliczny(100, 'Michał', 'Mazur', 'Częstochowa Pużaka 13 m 12', 929292929)
p1 = Produkt(12, 'laptop', '02-03-2020', '2 kg', 2799.99)
p2 = Produkt(14, 'myszka', '04-11-2017', '0,2 kg', 39.99)

z1=Zamowienie
z1.nr_zamowienia=11
z1.klient=k1
z1.produkty=[p1,p2]
z1.data_zamowienia='08-11-2021'
z1.stan='do realizacji'

print(str(z1))
