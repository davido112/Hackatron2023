from defines import clear, alap
import sys

hossz, szel = alap("", "")
while True:
    data = input("Hova?\n")

    if data.lower() == "balra":
        if szel < 2:
            szel -= 1
            hossz, szel = alap(hossz, szel)
            print("Most ennyi volt, szép napot!")
            break
        else:
            szel -= 1
            clear()
    elif data.lower() == "jobbra":
        if szel > 58:
            szel += 1
            hossz, szel = alap(hossz, szel)
            print("Most ennyi volt, szép napot!")
            break
        else:
            szel += 1
            clear()
    elif data.lower() == "fel":
        if hossz < 1:
            hossz -= 1
            hossz, szel = alap(hossz, szel)
            print("Most ennyi volt, szép napot!")
            break
        else:
            hossz -= 1
            clear()
    elif data.lower() == "le":
        if hossz > 28:
            hossz += 1
            hossz, szel = alap(hossz, szel)
            print("Most ennyi volt, szép napot!")
            break
        else:
            hossz += 1
            clear()
    elif data.lower() == "meguntam":
        break
    else:
        None
    hossz, szel = alap(hossz, szel)