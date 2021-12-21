from klasy.Diata import Dieta
from klasy.Dietetyk import Dietetyk
from klasy.Pacjent import Pacjent
from klasy.Zamowienie import Zamowienie


pacjent1 = Pacjent("Adam", "Małysz", "111222333", "ul. Bukowa 100 m 10")
dietetyk1 = Dietetyk("Gordon", "Ramsey", "666219827", "2019-03-17")

dieta1 = Dieta("Slim Standard", "Dieta dla każdego!", 1500, 210.00)
dieta2 = Dieta("Slim Hashimoto", "Dieta dla osób z chorobami tarczycy.",
               1800, 220.50)

zamowienie = Zamowienie()
zamowienie.nr_zamowienia = 12
zamowienie.data = "2021-12-21"
zamowienie.diety = [dieta1, dieta2]
zamowienie.pacjent = pacjent1
zamowienie.dietetyk = dietetyk1

print(zamowienie)
