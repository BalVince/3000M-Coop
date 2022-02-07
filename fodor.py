def feladat_1(lista):
    return len(lista)

# 1)	Hány település található az input fájlban?
feladat_1(Település.lista)

def feladat_2_3(lista, rang):
    sum = 0
    for elem in lista:
        if elem.rang == rang:
            sum += 1
    return sum

# 2)	Hány község rangú település található?
feladat_2_3(Település.lista, "község")
# 3)	Hány város rangú település található?
feladat_2_3(Település.lista, "város")

def feladat_4(lista):
    i = 0
    while i < len(lista) and lista[i].rang != "falu":
        i += 1
    return i < len(lista)

# 4)	Van-e falu rangú település?
feladat_4(Település.lista)

def feladat_5_10(lista, rang, nev):
    sum = 0
    for elem in lista:
        if elem.rang == rang and elem.nev == nev:
            sum += 1
    return sum

# 5)	Hány község rangú település található a Makói kistérségben?
feladat_5_10(Település.lista, "község", "Makói")
# 6)	Hány község rangú település található a Szegedi kistérségben?
feladat_5_10(Település.lista, "község", "Szegedi")
# 7)	Hány község rangú település található a Szentesi kistérségben?
feladat_5_10(Település.lista, "község", "Szentesi")
# 8)	Hány város rangú település található a Makói kistérségben?
feladat_5_10(Település.lista, "város", "Makói")
# 9)	Hány város rangú település található a Szegedi kistérségben?
feladat_5_10(Település.lista, "város", "Szegedi")
# 10)	Hány város rangú település található a Szentesi kistérségben?
feladat_5_10(Település.lista, "város", "Szentesi")

def feladat_11_12_p(lista, rang, nepesseg):
    for elem in lista:
        if elem.rang == rang and elem.népessége > nepesseg:
            print(f"{elem.nev}, {elem.népessége}")

# 11)	Írja ki a község rangú települések közül az 1000 főnél népesebb települések nevét és népességét!
feladat_11_12_p(Település.lista, "község", 1000)
# 12)	Írja ki a város rangú települések közül az 10000 főnél népesebb települések nevét és népességét!
feladat_11_12_p(Település.lista, "város", 10000)

def feladat_13_14_p(lista, rang, nepesseg):
    for elem in lista:
        if elem.rang == rang and elem.népessége < nepesseg:
            print(f"{elem.nev}, {elem.népessége}")

# 13)	Írja ki a község rangú települések közül az 1000 főnél alacsonyabb népességű települések nevét és népességét!
feladat_11_12_p(Település.lista, "község", 1000)
# 14)	Írja ki a város rangú települések közül az 5000 főnél alacsonyabb népességű települések nevét és népességét!
feladat_11_12_p(Település.lista, "város", 5000)