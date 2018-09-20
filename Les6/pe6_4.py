i = False


def new_password(x, y):
    if x not in y:
        if len(y) >= 6:
            for c in y:
                if c in "0123456789":
                    i = True
                    if i == True:
                        print("Uw wachtwoord is succesvol veranderd.")
                    else:
                        print("Uw wachtwoord moet minimaal 1 cijfer bevatten.")
        else:
            print("Uw nieuwe wachtwoord moet minimaal 6 tekens bevatten.")
    else:
        print("Uw nieuwe wachtwoord mag niet hetzelfde zijn als uw oude wachtwoord.")


oldpassword = input("Uw oude wachtwoord: ")
newpassword = input("Uw nieuwe wachtwoord: ")
new_password(oldpassword, newpassword)
