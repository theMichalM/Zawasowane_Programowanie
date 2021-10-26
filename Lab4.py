#Zadanie 1
print("zadanie 1:")
class Student:
    def __init__(self, name, mark) -> None:
        self.name = name
        self.mark = mark
    def is_passed(self) -> bool:
        if self.mark>50:
            return True
        else:
            return False
    def __str__(self) -> str:
        return f'Imie: {self.name}, Mark: {str(self.mark)}'
s1 = Student('Michał', 90)
s2 = Student('Kacper', 40)
print(s1.is_passed())
print(s2.is_passed())

#Zadanie 2
print("\nzadanie 2:")
class Library:
    def __init__(self,city,street, zip_code,open_hours:str,phone) -> None:
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone
    def __str__(self) -> str:
        return f'City: {self.city}, Street: {self.street}, Zip code: {self.zip_code}, Open hours: {self.open_hours}, Phone: {str(self.phone)}'

class Employee:
    def __init__(self,first_name, last_name, hire_date, birth_date, city, street, zip_code, phone:int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone
    def __str__(self) -> str:
        return f'Name: {self.first_name} {self.last_name}, Hire date: {self.hire_date}, Birth date: {self.birth_date}, City: {self.city}, Street: {self.zip_code}, Phone: {self.phone}'

class Book:
    def __init__(self, library:Library, publication_date, author_name, author_surname, number_of_pages) -> None:
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages
    def __str__(self) -> str:
        return f'Library: {str(self.library)}\nPublication date: {self.publication_date}, Author: {self.author_name}{self.author_surname}, Number of pages: {str(self.number_of_pages)}'

class Order:
    def __init__(self,employee:Employee,student:Student,books:list,order_date) -> None:
        self.employee:Employee = employee
        self.student:Student = student
        self.books:list = books
        self.order_date = order_date
    def __str__(self) -> str:
        bookstr:str = ''
        for b in self.books:
            bookstr += str(b)+'\n'
        return f'Zamówienie: \nEmployee: \n{str(self.employee)}\nStudent: \n{str(self.student)}\nBooks: \n{bookstr}Order date: {self.order_date}\n'

l1 = Library('Katowice', 'Plac Rady Europy 1', '40-021', '10:00 - 18:00', 322083740)
l2 = Library('Częstochowa', 'Aleja Armii Krajowej 36', '42-201', '08:30–19:00', 343250957)

mitologia = Book(l1, '1992', 'Jan', 'Parandowski', 304)
cpp = Book(l2, '2012-12-20', 'Stephen', 'Prat', 1200)
wiedzmin = Book(l1, '1993', 'Andrzej', 'Sapkowski', 330)
python = Book(l2, '2020-06-02', 'Eric', 'Matthes', 616)
harry_potter = Book(l1,'26 czerwca 1997','Joanne Kathleen','Rawling',326)

e1 = Employee('Robert', 'Nowak', '12-02-2005', '03-05-1990', 'Katowice', '1 Maja', '40-021', '111222333')
e2 = Employee('Agata', 'Kowalska', '12-05-2006', '06-11-1983', 'Katowice', '3 Maja', '40-021', '113252363')
e3 = Employee('Kamil', 'Zawadzki', '23-09-2004', '08-05-1972', 'Częstochowa', 'Polskiego Czerwonego Krzyrza', '42-201', '415236743')

s3 = Student('Julia', 78)

z1 = Order(e1,s1,[mitologia,harry_potter],'28-10-2021')
z2 = Order(e3,s3,[cpp,python],'29-10-2021')
print(z1)
print(z2)

print('\nZadanie 3')
class Property:
    def __init__(self, area, rooms:int, price, address) -> None:
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address
    def __str__(self) -> str:
        return f'Area: {self.area}, rooms: {str(self.rooms)}, price: {str(self.price)}, address: {self.address}'

class Hause(Property):
    def __init__(self, area, rooms: int, price, address, plot:int) -> None:
        super().__init__(area, rooms, price, address)
        self.plot = plot
    def __str__(self) -> str:
        return super().__str__() + ', plot: ' + str(self.plot)

class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor) -> None:
        super().__init__(area, rooms, price, address)
        self.floor = floor
    def __str__(self) -> str:
        return super().__str__() + ', floor: ' + str(self.floor)

hause = Hause('Częstochowa', 5, '200 000zł', 'Polna 3', 20)
flat = Flat('Częstochowa', 5, '50 000zł', 'Waszynktona 20', 10)
print(flat)
print(hause)