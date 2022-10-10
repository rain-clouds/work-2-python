import random

def init(n):
    # casutele solide
    Matrix = [[0 for i in range(n)] for j in range(n)]
    print(Matrix)
    g=random.randint(0,n/2-1)
    #gheata
    for i in range(0,g):
        corect =0
        while corect==0:
            x=random.randint(0,n-1)
            y=random.randint(0,n-1)
            if Matrix[x][y]==0:
                Matrix[x][y]=1
                corect=1

    return Matrix


def next(Matrix,n,pozii,pozij,a):
    if(a=="st"):
        if pozij==0:
            print("miscare gresita")
        else:
            pozij=pozij-1

    if (a == "dr"):
        if pozij == n-1:
            print("miscare gresita")
        else:
            pozij = pozij + 1

    if (a == "s"):
        if pozii == 0:
            print("miscare gresita")
        else:
            pozii = pozii - 1

    if (a == "j"):
        if pozii == n-1:
            print("miscare gresita")
        else:
            pozii = pozii + 1
    return pozii,pozij


def rezolvare():
    n = int(input())

    Matrix=init(n)
    print(Matrix)
    print()

    # playerul
    pozii = random.randint(0, n-1)// 0
    pozij = random.randint(0, n-1)
    print(pozii)
    print(pozij)
    print()
    # finish
    pozfi = random.randint(0, n-1)
    pozfj = random.randint(0, n-1)

    a=input()
    pozii,pozij=next(Matrix,n,pozii,pozij,a)
    print(pozii)
    print(pozij)

rezolvare()