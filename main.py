class Település:
    lista = []
    def __init__(self, azonosito, nev, rang, kistbes, területe, népessége, lakásszám):
        self.azonosito = azonosito
        self.nev = nev
        self.rang = rang
        self.kistbes = kistbes # kistérségi besorolás
        self.területe = területe # terület hektárban
        self.népessége = népessége
        self.lakásszám = lakásszám
        Település.lista.append(self)

with open("input.txt", "r", encoding="utf8") as f:
    for sor in f:
        s = sor.strip().split("\t")
        t = Település(int(s[0]), s[1], s[2], s[3], int(s[4]), int(s[5]), int(s[6]))