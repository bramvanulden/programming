

def convert(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit
def table():
    print("F \t\t C")
    for temperatuur in range(-30, 40, 10):
        print(convert(temperatuur), "\t",temperatuur)

table()