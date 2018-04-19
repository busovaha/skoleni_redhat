#vlastnosti, ktere lze menit pri volani z prikazoveho radku
import argparse

tridy = {1:"prima", 2:"sekunda", 3:"tercie", 4:"kvarta", 5:"kvinta", 6:"sexta"}


def nazev_tridy(n, v):
    if v:
        print("Nazev tridy v gvid je:")
    print(tridy[n])


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--vice-info", action="store_true")

    parser.add_argument("--tridy", type=int)
    args = parser.parse_args()
    print("Gymnazium Brno Videnska")


    if args.tridy:
        nazev_tridy(args.tridy, args.vice_info)



if __name__ == "__main__":
    # execute only if run as a script
    main()

