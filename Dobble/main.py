from itertools import combinations
import re
import math
# Bekérem az adatokat amik szükségesek a kártya pakli generáláshoz
n = int(input("Mennyi szám legyen egy kártyán?\n"))
max = int(input("Mekkora legyen a legnagyobb szám?\n"))+1

data = []
for i in range(max):
    data.append(i)

egesz = len(data)

kombinaciok_szama = math.comb(egesz, n)
valasz = ""
if kombinaciok_szama > 100:
    valasz = input(f"Figyelem! Több mint száz({kombinaciok_szama}) lehetőség van. Ki szeretnéd generálni mindet? Igen/Nem (ENTER = Nem)")
    if valasz == "":
        valasz = "nem"
    elif valasz == "igen":
        valasz = "igen"
    else:
        valasz = "nem"

if valasz.lower() == "igen" or valasz == "":
    kombinaciok = list(combinations(data, n))
    for i in range(len(kombinaciok)):
        print(re.sub("[(),]", "", str(kombinaciok[i])))