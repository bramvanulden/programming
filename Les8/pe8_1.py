def seizoen(maand):
    if maand == 12 or maand <= 3:
        print("De maand valt in de winter.")
    elif maand > 3 and maand < 7:
        print("De maand valt in de lenter")
    if maand < 10 and maand > 6:
        print("De maand valt in de zomer.")
    if maand >= 10 or maand < 12:
        print("De maand valt in de herfst.")

maand = int(input("Vul het nummer van de maand in: "))
seizoen(maand)