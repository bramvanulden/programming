invoer = "5-9-7-1-7-8-3-2-4-8-7-9"


def informatie(invoer):
    lijst=[]
    for c in invoer.split('-'):
        lijst.append(int(c))
    print(sorted(lijst))
    print("Grootste getal:", max(lijst), "en kleinste getal:", min(lijst))
    print("Aantal getallen:", len(lijst), "en de som van de getallen:", sum(lijst))
    print("Gemiddelde:", sum(lijst) / len(lijst))


informatie(invoer)
