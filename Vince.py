# 15)	Mennyi a legnépesebb település lélekszáma?

def feladat_15(lista):
    temp = lista[0]
    for i in lista[1:]:
        if temp.népessége < i.népessége:
            temp = i
    return temp.népessége

# 16)	Mennyi a legalacsonyabb népességű település lélekszáma?

def feladat_16(lista):
    temp = lista[0]
    for i in lista[1:]:
        if i.népessége < temp.népessége:
            temp = i
    return temp.népessége

# 17)	Melyik a legnépesebb település? Írja ki a település nevét és lélekszámát!

def feladat_17(lista):
    temp = lista[0]
    for i in lista[1:]:
        if temp.népessége < i.népessége:
            temp = i
    return (temp.nev,temp.népessége)


# 18)	Melyik a legalacsonyabb népességű település? Írja ki a település nevét és lélekszámát!

def feladat_17(lista):
    temp = lista[0]
    for i in lista[1:]:
        if i.népessége < temp.népessége:
            temp = i
    return (temp.nev,temp.népessége)

# 19)	Melyik a Makói kistérség legkisebb területű települése(i)?

def KistéerségLegnéptelenebbTelepülése(lista, kistérség):
    temp = ""
    for i in lista:
        if i.kistbes == kistérség:
            if temp == "" or i.népesség < temp.népesség:
                temp = i
    temp2 = []
    for i in lista:
        if i.kistbes == kistérség and i.népesség == temp.népesség:
            temp2.append(i.nev)

def feladat_19(lista):
    return KistéerségLegnéptelenebbTelepülése(lista, "Makói")


# 20)	Melyik a Szegedi kistérség legkisebb területű települése(i)?

def feladat_20(lista):
    return KistéerségLegnéptelenebbTelepülése(lista, "Szegedi")


# 21)	Melyik a Szentesi kistérség legkisebb területű települése(i)?

def feladat_21(lista):
    return KistéerségLegnéptelenebbTelepülése(lista, "Szentesi")


# 22)	Melyik a Makói kistérség legnépesebb települése(i)?

def KistéerségLegnépesebbTelepülése(lista, kistérség):
    temp = ""
    for i in lista:
        if i.kistbes == kistérség:
            if temp == "" or i.népesség > temp.népesség:
                temp = i
    temp2 = []
    for i in lista:
        if i.kistbes == kistérség and i.népesség == temp.népesség:
            temp2.append(i.nev)

def feladat_22(lista):
    return KistéerségLegnépesebbTelepülése(lista, "Makói")

# 23)	Melyik a Szegedi kistérség legnépesebb települése(i)?

def feladat_23(lista):
    return KistéerségLegnépesebbTelepülése(lista, "Szegedi")

# 24)	Melyik a Szentesi kistérség legnépesebb települése(i)?

def feladat_24(lista):
    return KistéerségLegnépesebbTelepülése(lista, "Szentesi")

# 25)	Írja ki a Makói kistérség településeinek népsűrűségét!



# 26)	Írja ki a Szegedi kistérség településeinek népsűrűségét!



# 27)	Írja ki a Szentesi kistérség településeinek népsűrűségét!



# 28)	Írja ki a Kisteleki kistérség településeinek népsűrűségét!


