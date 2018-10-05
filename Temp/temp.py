def bmi(gewicht, lengte):
    bmi = (gewicht * 703) / (lengte ** 2)
    if bmi < 18.5:
        print("Underweight")
    elif bmi > 20.5:
        print("Overweight")
    else:
        print("Perfect gewicht")


gewicht = int(input("Uw gewicht(ponden): "))
lengte = int(input("Uw lengte(inches): "))
bmi(gewicht, lengte)
