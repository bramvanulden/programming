def gemiddelde(zin):
    woorden = zin.split()
    for c in woorden:
        letters = + len(c)
        hoeveelheidwoorden = + 1
    gem = letters / hoeveelheidwoorden
    print("De gemiddelde lengte van de woorden in deze zin is: ", gem)


inputzin = input("Typ hier een willekeurige zin: ")
gemiddelde(inputzin)
