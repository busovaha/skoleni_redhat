#slovnik
jmena = ["hana", "petr", "pepa", "ivo", "tom", "anna", "anezka", "barbora", "eva", "majkl", "karolina"]

my_dict={}
for i in jmena:
    my_dict[i]=len(i)

print(my_dict)

reverse_dict={}

def check_key(a):
    if a in reverse_dict.keys():
        return True
    return False

for i in my_dict:
    if not check_key(my_dict[i]):
        reverse_dict[my_dict[i]] = []
    reverse_dict[my_dict[i]].append(i)

for k, v in reverse_dict.items():
    print(str(k) + "..." + str(v))

print(reverse_dict)
def jmena_delky(n=4):
        sezn = [jmeno for jmeno in my_dict if my_dict[jmeno] == n]
        return sezn

print(jmena_delky(5))


def get_integer(help_text="Give me a number: "):
    return int(input(help_text))

print(get_integer())
n=get_integer("dej mi cislo:")
print(n)