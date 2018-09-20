getallen = [4, 5, 3, -81]
lijst = [0]
nieuwelijst = [0]


def kwadraten_som(grondgetallen):
    for c in grondgetallen:
        if c >= 0:
            lijst.append(c)
    nieuwelijst = [i ** 2 for i in lijst]
    print(sum(nieuwelijst))

kwadraten_som(getallen)
