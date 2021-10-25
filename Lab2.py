#Zadanie 2.a.
def zada(lista):
    for x in lista:
        print(x)
l1 = ["Michał","Ada","Aneta","Mariusz","Anna"]
zada(l1)

#Zadanie 2.b.
def zadb1(lista):
    for x in lista:
        print(x*2)
l2=[1,2,3,4,5]
zadb1(l2)

def zadb2(lista):
    listab = [2*x for x in lista]
    print(listab)
zadb2(l2)

#Zadanie 2.c.
def zadc():
    for x in range(10):
        if x%2==0:
            print(x)
zadc()

#Zadanie 2.d.
def zadd():
    for x in range(0,10,2):
        print(x)
zadd()