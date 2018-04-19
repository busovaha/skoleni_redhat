#print-format
jmena = ["hana", "petr", "pepa", "ivo", "tom", "anna", "anezka", "barbora", "eva", "majkl", "karolina"]

my_dict={}
for i in jmena:
    my_dict[i]=len(i)

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
    #print(str(k) + "..." + str(v))
    print("{a}...{b}".format(a = k, b = v))
print(reverse_dict)
