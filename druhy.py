import sys
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def first(sez, n=5):
    newsez = [number for number in sez if number < n]
    print(type(newsez))
    return newsez

print(first(a, int(sys.argv[1])))

