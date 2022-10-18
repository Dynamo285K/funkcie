
def komb(cislo:int,b):
    for i in range(cislo):
        print(b,end="")


    print('')
    for i in range(0,31,):
        if i == 0 or i % 30 == 0:
            print(b)
        else:
            print(" ")

    print('')





komb(30,"#")
