class Település:
    lista = []
    def __init__(self, azonosito, nev, rang, kistbes, területe, népessége, lakásszám):
        self.azonosito = azonosito
        self.nev = nev
        self.rang = rang
        self.kistbes = kistbes
        self.területe = területe
        self.népessége = népessége
        self.lakásszám = lakásszám
        Település.lista.append(self)

with open("input.txt", "r", encoding="utf8") as f:
    for sor in f:
        s = sor.strip().split("\t")
        t = Település(int(s[0]), s[1], s[2], s[3], int(s[4]), int(s[5]), int(s[6]))
"""
def feladat_29(lista):
    for elem in lista:
        if elem.kistbes == "Makói" and elem.népessége < 1000:
            return False
    return True

def feladat_30(lista):
    for elem in lista:
        if elem.kistbes == "Szentesi" and elem.népessége < 10000:
            return False
    return True

def feladat_31(lista):
    for elem in lista:
        if elem.kistbes == "Szegedi" and elem.népessége < 2000:
            return False
    return True

def feladat_32(lista):
    for elem in lista:
        if elem.kistbes == "Kisteleki" and elem.népessége < 10000:
            return False
    return True

def feladat_33(lista):
    for elem in lista:
        if elem.kistbes == "Makói":
            print(f"{elem.nev}: {round(elem.népessége / elem.lakásszám, 2)}")

def feladat_34(lista):
    for elem in lista:
        if elem.kistbes == "Szentesi":
            print(f"{elem.nev}: {round(elem.népessége / elem.lakásszám, 2)}")

def feladat_35(lista):
    for elem in lista:
        if elem.kistbes == "Szegedi":
            print(f"{elem.nev}: {round(elem.népessége / elem.lakásszám, 2)}")

def feladat_36(lista):
    for elem in lista:
        if elem.kistbes == "Kisteleki":
            print(f"{elem.nev}: {round(elem.népessége / elem.lakásszám, 2)}")

def feladat_37(lista):
    x = ""
    y = 0
    for elem in lista:
        if (elem.népessége / elem.lakásszám) > y:
            y = elem.népessége / elem.lakásszám
            x = elem.nev
    return x

def feladat_38(lista):
    listasd = {}
    for elem in lista:
        if elem.kistbes in listasd.keys():
            listasd[elem.kistbes] += 1
        else:
            listasd[elem.kistbes] = 1
    return listasd

def feladat_39(lista):
    listasd = {}
    for elem in lista:
        if elem.kistbes in listasd.keys():
            listasd[elem.kistbes] += elem.népessége
        else:
            listasd[elem.kistbes] = elem.népessége
    return listasd

def feladat_40(lista):
    listasd = {}
    for elem in lista:
        if elem.kistbes in listasd.keys():
            listasd[elem.kistbes] += elem.területe
        else:
            listasd[elem.kistbes] = elem.területe
    return listasd
"""
def feladat_29k(lista): return len([elem for elem in lista if elem.kistbes == "Makói" and elem.népessége < 1000]) == 0
    #return len([elem for elem in lista if elem.kistbes == "Makói" and elem.népesség >= 1000]) == len([elem for elem in lista if elem.kistbes == "Makói"])
def feladat_30k(lista): return len([elem for elem in lista if elem.kistbes == "Szentesi" and elem.népesség < 10000]) == 0
def feladat_31k(lista): return len([elem for elem in lista if elem.kistbes == "Szegedi" and elem.népesség < 2000]) == 0
def feladat_32k(lista): return len([elem for elem in lista if elem.kistbes == "Kisteleki" and elem.népesség < 10000]) == 0
def feladat_33k(lista): return 
def feladat_34k(lista):
    for elem in [elem for elem in lista if elem.kistbes == "Szentesi"]:
        print(f"{elem.nev}: {round(elem.népessége / elem.lakásszám, 2)}")
