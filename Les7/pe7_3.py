def fetchdata(file):
    infile = open(file, "r")
    lijst = infile.readlines()
    infile.close()
    print("Het grootste kaartnummer is:", max(lijst)[0:6])
    print("Deze file telt", len(lijst), "regels.")

file = "Kaartnummers.txt"
fetchdata(file)