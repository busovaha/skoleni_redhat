def zadej_cislo(text, v):
    while True:
        x = int(input(text)) - 1
        if x > v:
            print("Zadej mensi cislo.")
        else:
            break
    return x

class Piskvorky:
    hrac = True #True=o False=x
    velikost = None
    pole=None

    def __init__(self, velikost):
        self.velikost=velikost

    def prvni_pole(self):
        self.pole=[]
        for i in range(0, self.velikost):
            self.pole.append([])

            for j in range(0, self.velikost):
                self.pole[i].append(0)
        print(self.pole)

    def zapis_znak(self, znak, x, y): # o=1 x=2
        self.pole[x][y]=znak

    def lichy_radek(self):
        print(" _" * n)

    def sudy_radek(self):
        print("| " * n + "|")

    def plan(self, velikost):
        for i in range(0, velikost):
            self.lichy_radek()
            self.sudy_radek()
        self.lichy_radek()

    def tisk_pole(self):
        for i in range (0, self.velikost):
            print(" -" * self.velikost)
            for j in range(0, self.velikost):
                print("|", end="")
                if self.pole[i][j]==2:
                    print("x", end="")
                elif self.pole[i][j]==1:
                    print("o", end="")
                else:
                    print(" ", end="")
            print("|")
        print(" -" * self.velikost)

    def control_win_radek(self,znak):

        for i in range (0, self.velikost):
            for j in range(0, self.velikost):
                if self.pole[i][j]==znak:
                    try:
                        count = len([r for r in range(0,3) if self.pole[i][j+r]==znak])

                    except IndexError:
                        return  False
                    if count>2:
                        return True
        return False
    def control_win_sloupec(self,znak):

        for i in range(0, self.velikost):
            for j in range(0, self.velikost):
                if self.pole[i][j] == znak:
                    try:
                        count = len([r for r in range(0, 3) if self.pole[i + r][j] == znak])
                    except IndexError:
                        return False
                    if count > 2:
                        return True
        return False

    def hrat(self):

        self.prvni_pole()
        while True:
            self.tisk_pole()
            print("Hraje hrac {a}".format(a= "o" if self.hrac else "x"))
            while True:
                x = zadej_cislo("Zadej souradnici x:", self.velikost)
                y = zadej_cislo("Zadej souradnici y:", self.velikost)
                if self.pole[x][y]!=0:
                    print("Policko je obsazene. Hrej znovu.")
                else:
                    break

            if self.hrac:
                self.zapis_znak(1, x, y)
                self.hrac=False
                if self.control_win_sloupec(1) or self.control_win_radek(1):
                    print("Vyhra!")
                    break
            else:
                self.zapis_znak(2, x, y)
                self.hrac=True
                if self.control_win_sloupec(2) or self.control_win_radek(2):
                    print("Vyhra!")
                    break



if __name__ == "__main__":

    n = int(input("Zadej velikost hraciho pole:"))
    p = Piskvorky(n)
    p.hrat()

