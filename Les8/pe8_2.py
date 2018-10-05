lijst = eval(input("Geef lijst met minimaal 10 strings: "))
nieuwelijst = list()
for c in lijst:
    if len(c) <= 4:
        nieuwelijst.append(c)

print(nieuwelijst)