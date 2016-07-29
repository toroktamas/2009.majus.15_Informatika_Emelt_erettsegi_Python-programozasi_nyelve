#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Elso feladat adat beimportalas. Egy szotarba gondolom beimportalni ami igy nezne ki:
lift={
    datetime(9 7 11){
        "csoport szam" = 7
        "indulo szint" = 6
        "celszint" = 22
    }
    datetime(9 10 30){
        "csoport szam" = 8
        "indulo szint" = 18
        "celszint" = 20
    }
    
}
"""
from datetime import datetime
import random
print("1. feladat")
lift = {}
n = 0
csapat_max_szam = int()
with open("igeny.txt", "rt+", encoding="utf-8") as f:
    for s in f:
        sor = s.replace("\n", "")
        n+=1
        if n == 2:
            csapat_max_szam = sor
        if n >= 4:
            sor = sor.split(" ")
            key = datetime(1900, 1, 1, int(sor[0]), int(sor[1]), int(sor[2]))            
            lift[key] = {}
            lift[key]["csoport szam"] = int(sor[3])
            lift[key]["indulo szint"] = sor[4]
            lift[key]["cel szint"] = sor[5]

#print(lift)
print("2. feladat")

hol_alt_a_lift = int(input("Kerem adja meg hogy a megfigyeles kezdeten hol alt a lift: "))

print("3. feladat")
"""Ki kell irni az utolso szintet ahol megalt vagyi az utolso celszintet"""
utolso_szint = 0
for a in sorted(lift.keys()):
    utolso_szint+=1
    if utolso_szint == len(lift):
        print("A lift a {}. szinten all az utolso igeny teljesitese utan.".format(lift[a]["cel szint"]))

print("4. feladat")
""" Ki kell iratni a kepernyore a legmagasabb es legalacsonyabb sorszamu szintet amit a lift erintett."""
erintett_szintek = [hol_alt_a_lift]
for v in lift.values():
    erintett_szintek.append(int(v["indulo szint"]))
    erintett_szintek.append(int(v["cel szint"]))
print("A legalacsonyabb sorszamu szint amit a lift erintett: {0}, es a legmagasabb szint amit a lift erintett: {1}. ".\
      format(min(erintett_szintek),max(erintett_szintek)))

print("5. feladat")
""" Meg kell hatarozni hogy hanyszor kellett felfele indulnia a liftnek utassal es utas nelkul."""
utassal_felfele = 0
utasnelkul_felfele = 0
elozo_celszint = hol_alt_a_lift
for v in lift.values():
    if int(v["indulo szint"]) > elozo_celszint:
        utasnelkul_felfele+=1

    if int(v["indulo szint"]) < int(v["cel szint"]):
        utassal_felfele += 1
        
    elozo_celszint = int(v["cel szint"])


print("A liftnek {0}-enyiszer kellett felmenni-e utassal es {1}-ennyiszer utas nelkul.".\
      format(utassal_felfele,utasnelkul_felfele))

print("6. feladat")
szerelocsapatok = []
lista_egytol_csapat_max_szam_ig = []
for v in lift.values():
    szerelocsapatok.append(int(v["csoport szam"]))
setszerelo = set(szerelocsapatok)
#print(setszerelo)

#print(lista_egytol_csapat_max_szam_ig)
nincs_benne = []

for a in range(1, int(csapat_max_szam)+1):
    if a not in setszerelo:
        nincs_benne.append(a)
        
print("Ezek a csoportok nem hasznaltak a liftet:{0}".format(nincs_benne))

print("7. feladat")
szotar ={}
a = random.choice(list(setszerelo))
print(a)

for k,v in lift.items():
    if v["csoport szam"] == int(a):
      szotar[k] = {}
      szotar[k]["indulas"] = v["indulo szint"]
      szotar[k]["erkezes"] = v["cel szint"]

if len(szotar) == 1:
    print("Nincs eleg adat a vizsgalathoz.")
else:
    n=0
    for a in sorted(szotar.keys()):    
        n+=1
        if n > 1:
            elozo_szint = szotar[a]["erkezes"]    
            if szotar[a]["indulas"] < elozo_szint or szotar[a]["indulas"] < elozo_szint:
                print("{0}-ik es a {1}-ik szint kozott setaltak az emberek szabalytalanul".format(elozo_szint, szotar[a]["indulas"]))
            else:
                print("Nem bizonyithato szabalytalansag.")

print("8. feladat")

with open("blokkol.txt", "rt+", encoding="utf-8") as f:
    for k in sorted(szotar.keys()):
        g = szotar[k]
        print("A jelen munkaidopontja {0} amihez kerjuk adja meg az alabbi adatokat.".format(datetime.strftime(k, "%H:%M:%S")))
        Feladatkod = int(input("Kerem adja meg a feladatkodot. "))
        Sikeresseg = str(input("Kerem adja meg hogy 'befejezett' vagy 'befejezetlen' az adott munka. "))
        f.write("Indulasi emelet: {} \n".format(g["indulas"]))
        f.write("Celemelet: {} \n".format(g["erkezes"]))
        f.write("Feladatkod: {} \n".format(Feladatkod))
        f.write("Befejezes ideje: {0}:{1}:{2} \n".format(k.hour, k.minute, k.second))
        f.write("Sikeresseg: {} \n".format(Sikeresseg))
        f.write("----- \n")
