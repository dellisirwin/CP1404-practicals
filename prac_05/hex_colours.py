HEX_COLOURS = {"AliceBlue": "fof8ff", "beige": "f5f5dc", "black": "oooooo"}
colours = input("What Colour?").upper()
while colours != "":
    if colours in HEX_COLOURS:
        print(colours, "is", HEX_COLOURS[colours])

