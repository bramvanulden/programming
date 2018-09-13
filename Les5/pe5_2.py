leeftijd = int(input("Geef je leeftijd:"))
paspoort = str(input("Nederlands paspoort?(ja/nee)"))
if leeftijd >= 18 and "ja" in paspoort:
    print("Gefeliciteerd, u mag stemmen!")
else:
    print("Helaas, u mag niet stemmen.")
