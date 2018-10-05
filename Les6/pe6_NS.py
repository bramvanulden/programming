
def standaardtarief(afstandKM):
        if afstandKM <= 0:
            print("Uw afstand moet hoger zijn dan 0.")
        else:
            if afstandKM <= 50:
                d = afstandKM * 0.8
            else:
                d = afstandKM * 0.6 + 60
        return d

def ritprijs(leeftijd, weekendrit, afstandKM):
    standaardtarief(kilometers)
    if weekendrit == True:
        if leeftijd < 12 or leeftijd >= 65:
            prijs = d * 0.65
        else:
            prijs = d * 0.6
    else:
        if leeftijd < 12 or leeftijd >= 65:
            prijs = d * 0.7
    print("Uw prijs bedraagt:", prijs, "euro.")

leeftijd = int(input("Wat is uw leeftijd? "))
kilometers = int(input("Hoeveel kilometer is uw ritafstand? "))
weekendrit = bool(input("Rijdt u in het weekend? (yes/no) "))
ritprijs(leeftijd, weekendrit, kilometers)

