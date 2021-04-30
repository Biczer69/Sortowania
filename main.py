import random
import time

def tablicowanie(ilosci):
    tablica = []
    for x in range(ilosci):
        tablica.append(random.randint(0,100))
    return tablica


def sortowanie_przez_w(tablica):
    for j in range(1,len(tablica)):
        temp = tablica[j]
        i = j-1
        while(i>=0 and tablica[i]>temp):
            tablica[i+1] = tablica[i]
            i -=1
        tablica[i+1] = temp
    return tablica


"""
for x in range(1):
    dlugosc_tablicy = 10
    tabliczka = tablicowanie(dlugosc_tablicy)
    print(sorted(tabliczka))
    print(sortowanie_przez_w(tabliczka))
    try:
        assert sortowanie_przez_w(tabliczka) == sorted(tabliczka)
    except AssertionError:
       print("nie zgadza się", x+1)
"""
dlugosc_listy = int(input())
tablica = tablicowanie(dlugosc_listy)
czas = time.time()
#sortowanie_przez_w(tablica)
print("dlugość trawnia sortowania = ", time.time()-czas," s")
czas = time.time_ns()
sorted(tablica)
print("dlugość trawnia sortowania = ", time.time_ns()-czas, "ns")


