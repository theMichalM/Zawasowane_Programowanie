from klasy.Student import Student
from klasy.Library import Library
from klasy.Employee import Employee
from klasy.Book import Book
from klasy.Order import Order
from klasy.House import House
from klasy.Flat import Flat
# Zadanie 1
print("zadanie 1:")

s1 = Student('Michał', 90)
s2 = Student('Kacper', 40)
print(s1.is_passed())
print(s2.is_passed())

# Zadanie 2
print("\nzadanie 2:")

l1 = Library('Katowice', 'Plac Rady Europy 1', '40-021',
             '10:00 - 18:00', 322083740)
l2 = Library('Częstochowa', 'Aleja Armii Krajowej 36',
             '42-201', '08:30–19:00', 343250957)

mitologia = Book(l1, '1992', 'Jan', 'Parandowski', 304)
cpp = Book(l2, '2012-12-20', 'Stephen', 'Prat', 1200)
wiedzmin = Book(l1, '1993', 'Andrzej', 'Sapkowski', 330)
python = Book(l2, '2020-06-02', 'Eric', 'Matthes', 616)
harry_potter = Book(l1, '26 czerwca 1997', 'Joanne Kathleen', 'Rawling', 326)

e1 = Employee('Robert', 'Nowak', '12-02-2005', '03-05-1990',
              'Katowice', '1 Maja', '40-021', '111222333')
e2 = Employee('Agata', 'Kowalska', '12-05-2006', '06-11-1983',
              'Katowice', '3 Maja', '40-021', '113252363')
e3 = Employee('Kamil', 'Zawadzki', '23-09-2004', '08-05-1972', 'Częstochowa',
              'Polskiego Czerwonego Krzyrza', '42-201', '415236743')

s3 = Student('Julia', 78)

z1 = Order(e1, s1, [mitologia, harry_potter], '28-10-2021')
z2 = Order(e3, s3, [cpp, python], '29-10-2021')
print(z1)
print(z2)
print('\nZadanie 3')

hause = House('Częstochowa', 5, '200 000zł', 'Polna 3', 20)
flat = Flat('Częstochowa', 5, '50 000zł', 'Waszynktona 20', 10)
print(flat)
print(hause)
