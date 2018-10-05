file = "kluizen.txt"
leesfile = open(file)
content = leesfile.readlines()
writefile = open(file, "a")
lines = open(file, "r").readlines()
import random


def toon_aantal_kluizen_vrij():
    count = len(open(file).readlines())
    over = 12 - count
    print("Er xijn nog", over, "kluisjes over,")


def nieuwe_kluis():
    kluisnummers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    rawlijst = []
    gebruikt = []
    wachtwoord = " "
    count = len(open(file).readlines())
    over = 12 - count
    if over > 0:
        for line in lines:
            rawlijst += line.split(";")
        for gegeven in rawlijst:
            if len(gegeven) <= 2:
                gebruikt.append(gegeven)
        while True:
            randomkluis = random.randint(1, 12)
            if randomkluis not in gebruikt:
                wachtwoord = input(str("Geef een wachtwoord op: "))
                if len(wachtwoord) < 4:
                    print("Uw wachtwoord moet minimaal 4 tekens hebben.")
                    continue
                print("U bent kluisnummer", randomkluis, "toegewezen.")
                writefile.write(str(randomkluis))
                writefile.write(";")
                writefile.write(wachtwoord)
                writefile.write("\n")
                break


print("1: Ik wil weten hoeveel kluizen nog vrij zijn")
print("2: Ik wil een nieuwe kluis")
print("3: Ik wil even iets uit mijn kluis halen")
print("4: Ik geef mijn kluis terug")


keuze = int(input("Voer uw keuze in: "))
if keuze == 1:
    toon_aantal_kluizen_vrij()

if keuze == 2:
    nieuwe_kluis()
