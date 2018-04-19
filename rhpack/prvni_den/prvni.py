#vyjimky

def jmenovek():

    jmeno = str(raw_input("Zadej jmeno: "))
    while True:
        try:
            vek = int(input("Zadej vek: "))
            if vek > 130 or vek < 18:
                print("Mas blby vek :).")
            else:
                break
        except SyntaxError:
            print("Spatny format veku. Zadej spravny:")
        except ValueError:
            print("Spatny format veku. Zadej cislo:")
        except KeyboardInterrupt:
            print("Opravdu zadej vek:")


    print("Me jmeno je " + jmeno.capitalize() + ". Vek je " + str(vek) + ".")

jmenovek()