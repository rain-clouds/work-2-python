# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# EX 1. o instanta ar putea fi : (3,1,0,1,0,1,0,1)

#                              (n,b,m1,f1,m2,f2,.....,mn,fn)
# n=nr de cupluri, b=malul pe care se afla barca 0 pentru stanga si 1 pentru dreapta
# mi= barbatul din cuplul i,    fi=femeia cdin cuplul i, cu 0<i<=n
# o persoana din cuplul i are valoarea 0 daca e pe malul stang si 1 daca e pe malul drept


# EX 2 Starea initiala (n,0,0,0,0....,0)
#                         0 de 2n+1 ori


# Starea finala (n,1,1,1,1.....,1)
#                 1 de 2n+1 ori





def init(n):
    c = [0 for x in range(2 * n + 2)]
    c[0] = n
    return(c)

def final(x):
    for i in range(1,2*n+2):
        if x[i]==0:
            return 0
    return 1



n = 3
v=init(n)
print(v)
rezultat=final(v)
print(rezultat)


# EX 3.

def transition(state, par1, par2):

    # tranzitie parametri
    if  state[par1] == 0:
        state[par1] = 1
    else:
        state[par1] = 0
    if par1!=par2:
        if state[par2] == 0:
            state[par2] = 1
        else:
            state[par2] = 0

    #tranzitie barca
    if state[1] == 0:
        state[1] = 1
    else:
        state[1] = 0
    return state

rezultat=[3, 1, 0, 1, 0, 1, 0, 0]
para1=para2=3
rezultat=transition(rezultat,para1,para2)
print(rezultat)
def validation(state, par1, par2):

    if(state[par1]!=state[par2]):
        return 0

    if(state[par1]!=state[1]):
        return 0

    nrm0 = nrf0 = nrc0 = 0  # numarul de barbati, femei si cupluri de pe malul stang este initializat cu 0
    nrm1 = nrf1 = nrc1 = 0  # numarul de barbati, femei si cupluri de pe malul drept este initializat cu 0

    for i in range(2, 2 * n + 2):
        if state[i] == 0:
            if i % 2 == 0:
                nrm0 += 1
            else:
                nrf0 += 1
                if state[i] == state[i - 1]:
                    nrc0 += 1
        else:
            if i % 2 == 0:
                nrm1 += 1
            else:
                nrf1 += 1
                if state[i] == state[i - 1]:
                    nrc1 += 1
    if nrm0 > nrc0:
        if nrf0 > nrc0:
            return 0

    if nrm1 > 0:
        if nrf1 > nrc1:
            return 0
    return 1


rezultat=[3, 1, 0, 1, 0, 1, 1, 0]
para1=para2=3

valoare=validation(rezultat,para1,para2)
print(valoare)

 #ex 4 bkt nu stiu cum fac sa iasa

#ex 5 ideea e ca trebuie sa facem din vectorii astia niste noduri care sa aiba mai multi succesori,
#apoi luam fiecare succesor si verificam daca e valid, daca nu e il taiem din lista de succesori. la fel facem si cu
#succesorii valizi care la randul lor nu au