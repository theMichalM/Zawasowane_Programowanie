print('\nZadanie 1:')
def zad1(name:str, surname:str):
    return "Cześć "+ name + " " + surname + "!"
msg = zad1("Michał","Mazur")
print(msg)

print('\nZadanie 2:')
def zad2(a:int, b:int):
    return a*b
print(zad2(5,11))

print('\nZadanie 3:')
def zad3(a:int):
    return True if a%2==0 else False
check:bool = zad3(6)
if check==True:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")

print('\nZadanie 4:')
def zad4(a:int, b:int, c:int):
    return True if a+b>=c else False
print(zad4(3,4,8))

print('\nZadanie 5:')
def zad5(l1:list,a:int):
    return True if a in l1 else False
print(zad5([1,2,3,4,5],3))

print('\nZadanie 6:')
def zad6(l1:list, l2:list):
    for a in l2:
        if a not in l1:
            l1.append(a)
    for x in range(len(l1)):
        l1[x]=l1[x]**2
    return l1
print(zad6([1,2,3,4],[2,5,3,6]))

print('\nZadanie 7:')
#zadanie 7
from pip._vendor import requests
url='https://api.openbrewerydb.org/breweries'

class Browary:
    def __init__(self,id,name,brewery_type,street,address_2,address_3, city, state,county_province,postal_code,country,longitude,phone,website_url,updated_at,created_at):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state = state
        self.county_province = county_province
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.phone = phone
        self.website_url = website_url
        self.updated_at = updated_at
        self.created_at = created_at
    def __str__(self):
        return 'Id: ' + self.id + ', Name: ' + self.name + ', Brewery type: ' + self.brewery_type + ', City: ' + self.city
def zad7():
    Tab = requests.get(url).json()
    browary:Browary = {}
    for i in range(len(Tab)):
        ob = Tab[i]
        browary[i]=Browary(ob['id'],ob['name'],ob['brewery_type'],ob['street'],ob['address_2'],ob['address_3'],ob['city'],ob['state'],ob['county_province'],ob['postal_code'],ob['country'],ob['longitude'],ob['phone'],ob['website_url'],ob['updated_at'],ob['created_at'])
    for x in browary:
        print(browary[x])
zad7()

print('\nZadanie 8:')
#zadanie 8
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--city", type=str, help="Loking for browery by city")
args = parser.parse_args()
if not args.city:
    print("Nie podano miasta")
else:
    url='https://api.openbrewerydb.org/breweries?by_city='+args.city
    zad7()