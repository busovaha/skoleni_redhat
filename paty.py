def lichy_radek():
    print(" ..." * n)

def sudy_radek():
    print("|   " * n + "|")

n = int(input("Zadej cislo: "))
for i in range(0, n):
    lichy_radek()
    sudy_radek()

lichy_radek()