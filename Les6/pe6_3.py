def lang_genoeg(x):
    if x >= 120:
        print("Je bent lang genoeg voor de attractie!")
    else:
        print("Sorry, je bent te klein!")


lengte = int(input("Wat is uw lengte in centimers? "))
lang_genoeg(lengte)
