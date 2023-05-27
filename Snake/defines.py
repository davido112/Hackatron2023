import random
from os import system, name

def alap(hossz, szel):
    # Alap adat az első pályához.
    lvl1 = ["**************************************************************", "*                                                            *", "*************************************************************"]
    # Mivel 2 féle adattal és felesleges lenne ketté bontani az egészet így egy feltétellel elválasztom
    if hossz == "" and szel == "":
        # Random letesszük valahol a kis pitont
        hossz = random.randint(1, 29)
        szel = random.randint(1, 59)
        # Legeneráljuk a pályát
        for data in lvl1:
            if "* " in data:
                for ground in range(0, 30):
                    if hossz == ground:
                        # Kicseréljük az adott sorban található adatot @-ra
                        piton = data[:szel] + "@" + data[szel + 1:]
                        print(piton)
                    else:
                        print(data)
            else:
                print(data)
    else:
        # Ez a rész akkor fut le amikor már megvolt a random lehelyezés és lépkedünk.
        for data in lvl1:
            if "* " in data:
                for ground in range(0, 30):
                    if hossz == ground:
                        # Kicseréljük az adott sorban található adatot @-ra
                        piton = data[:szel] + "@" + data[szel + 1:]
                        print(piton)
                    else:
                        print(data)
            else:
                if hossz == -1:
                    # Kicseréljük az adott sorban található adatot @-ra
                    piton = data[:szel] + "@" + data[szel + 1:]
                    print(piton)
                elif hossz == 30:
                    # Kicseréljük az adott sorban található adatot @-ra
                    piton = data[:szel] + "@" + data[szel + 1:]
                    print(piton)
                else:
                    print(data)
    return hossz, szel
# Megkülönböztetjük az operációs rendszereket és töröljük a konzolt
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')