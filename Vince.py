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



# 20)	Melyik a Szegedi kistérség legkisebb területű települése(i)?



# 21)	Melyik a Szentesi kistérség legkisebb területű települése(i)?



# 22)	Melyik a Makói kistérség legnépesebb települése(i)?



# 23)	Melyik a Szegedi kistérség legnépesebb települése(i)?



# 24)	Melyik a Szentesi kistérség legnépesebb települése(i)?



# 25)	Írja ki a Makói kistérség településeinek népsűrűségét!



# 26)	Írja ki a Szegedi kistérség településeinek népsűrűségét!



# 27)	Írja ki a Szentesi kistérség településeinek népsűrűségét!



# 28)	Írja ki a Kisteleki kistérség településeinek népsűrűségét!


