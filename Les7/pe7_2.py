def lijst(file):
    infile = open(file, "r")
    content = infile.readlines()
    infile.close()
    for c in content:
        c.split(",")
        print(c[8:-1], "heeft kaartnummer:",c[:6])


file = "Kaartnummers.txt"
lijst(file)