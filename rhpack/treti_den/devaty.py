def dekorator(text, *args, **kwargs):
    print(text)
    print(args)
    print("Tisknu kwargs:")

    for i in kwargs:
        print("kwargs {k} {v}".format(k=i, v=kwargs[i]))

#dekorator("ahoj")
kwargs = {"1" :"a", "2":"b"}
dekorator("jee", "10000", "3019", c=100, **kwargs)
