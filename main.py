def stars(riadok:int):
    for i in range(riadok,):
        for i in range(riadok-i):
            print(end=" ")
        for i in range(5-i,5+i):
            print('*')



    print('')






stars(5)
