def pocetslov(sez):
    pocet = sum([len(i.split(" ")) for i in sez])
    """
    pocet=0
    for i in sez:
        pocet += len(i.split(" "))"""
    return pocet


with open("treti.py") as soubor:
    radky = soubor.readlines()
    radky = [x.strip() for x in radky]

    for i in radky:
        print(i)
    print("Pocet slov je:" + str(pocetslov(radky)))



