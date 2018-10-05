studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]


def gemiddelde_per_student(studentencijfers):
    antw = []
    for c in studentencijfers:
        antw.append(sum(c) / len(c))
    return antw


def gemiddelde_van_alle_studenten(studentencijfers):
    cijfers = int((studentencijfers[0] + studentencijfers[1] + studentencijfers[2]))
    hoeveelheid = int(len(studentencijfers[0]) + len(studentencijfers[1]) + len(studentencijfers[2]))
    gemiddelde = cijfers / hoeveelheid
    print(gemiddelde)


print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))