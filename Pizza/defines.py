import sys
def ellenorzes(data):
    meretek = ("kis", "kicsi", "közepes", "nagy", "pizza", "pizzát")
    feltetek = ("kolbászos", "kolbász", "tojásos", "tojás" "tojásal", "kukoricás", "kukorica", "gombás", "gomba", "sonkás", "sonka")
    italok = ("kóla", "kólát", "fanta", "fantát", "sprite", "spriteot")
    arak = {
        "kis" : 500,
        "kicsi" : 500,
        "közepes" : 750,
        "nagy" : 800,
        "pizza" : 500,
        "pizzát" : 500,
        "kóla" : 250,
        "kólát" : 250,
        "fanta" : 250,
        "fantát" : 250,
        "sprite" : 250,
        "spriteot" : 250,
        "kolbászos" : 100,
        "kolbász" : 100,
        "tojásos" : 200,
        "tojással" : 200,
        "kukorica": 150,
        "kukoricás": 150,
        "gomba" : 150,
        "gombás" : 150,
        "sonkás" : 250,
        "sonka" : 250
    }

    meret = ""
    ital = ""
    osszeg = 0
    data = data.replace(",", "")
    data = data.replace(".", "")
    data = data.replace("!", "")
    data = data.split(" ")
    tisztaadat = []
    for szavak in data:
        adat = tisztitas(szavak)
        tisztaadat.append(adat)


    for adatok in meretek:
        if adatok in tisztaadat:
            osszeg += arak[adatok]
            adatok = adatok.replace("át", "a")
            meret += adatok + " "
    for adatok in feltetek:
        if adatok in tisztaadat:
            adatok = adatok.replace("át", "a")
            osszeg += arak[adatok]
            print(adatok)
            meret += adatok + ", "
    for adatok in italok:
        if adatok in tisztaadat:
            osszeg += arak[adatok]
            adatok = adatok.replace("át", "a")
            ital += adatok+ ","

    return osszeg, meret, ital

def tisztitas(data:str):
    harom = ('ban', "sal", 'ben', 'ból', 'ből', 'ról', 'ről', 'nál', 'nél', 'hoz', 'hez', 'höz', 'tól', 'től', 'val', 'vel', 'kor', 'nak', 'nek')
    ketto = ('ba', 'be', 'on', 'en', 'ön', 'ra', 're', "al")
    tisztitott = data
    mod = 0
    for delete in harom: # Valamiért eltávolítja az utlsó 3 karaktert a kukorica-ról. Szia! Egy nagy kolbászos pizzát kérek kukorica feltéttel
        hossz = len(data)
        if delete in data[-3:]:
            tisztitott = data[:hossz-3] + "" + data[hossz + 1:]
            print(tisztitott)
            mod += 1
    for delete in ketto:
        hossz = len(data)
        if delete in data[-2:] and mod == 0:
            tisztitott = data[:hossz-2] + "" + data[hossz + 1:]
    if tisztitott[-1] == "á":
        tisztitott += "s"
    print(tisztitott)
    #print(tisztitott)
    return tisztitott