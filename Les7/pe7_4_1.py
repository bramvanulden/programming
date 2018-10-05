import datetime
vandaag = datetime.datetime.today()
datum = vandaag.strftime("%a %d %b %Y")
tijd = vandaag.strftime("%X")


def schrijfhardloper(hardloper):
    outfile = open("Hardlopers.txt", "a")
    outfile.write(str(datum) + ", " + str(tijd) + ", " + str(hardloper) + "\n")


while True:
    sprinter = input("Welke hardloper? ")
    schrijfhardloper(sprinter)