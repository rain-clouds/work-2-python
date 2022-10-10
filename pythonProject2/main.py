# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
B=[[0],[0],[0]]
X=[[0],[0],[0]]
A=[[0,0,0],
   [0,0,0],
   [0,0,0]]
AT=[[0,0,0],[0,0,0],[0,0,0]]
AS=[[0,0,0],[0,0,0],[0,0,0]]
AI=[[0,0,0],[0,0,0],[0,0,0]]


def det3(M):
    determinant=M[0][0]*M[1][1]*M[2][2]+M[1][0]*M[2][1]*M[0][2]+M[0][1]*M[1][2]*M[2][0]-(M[0][2]*M[1][1]*M[2][0]+M[0][1]*M[1][0]*M[2][2]+M[0][0]*M[1][2]*M[2][1])
    return determinant

def det2M(i,j,M):
    det=[[0,0],[0,0]]
    det2=-333
    ok=0
    for x in range(0,3):
        for y in range(0,3):
            if(x!=i and y!=j):
                if ok==0:
                    det[0][0]=M[x][y]
                elif ok==1:
                    det[0][1]=M[x][y]
                elif ok==2:
                    det[1][0]=M[x][y]
                elif ok==3:
                    det[1][1]=M[x][y]
                    det2 = det[0][0] * det[1][1] - det[0][1] * det[1][0]
                    return det2

                ok=ok+1
    print (det)
    print(det2)

def transpusa(M):
    transp = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for x in range(0,3):
        for y in range(0,3):
            transp[x][y]=M[y][x]
    return transp


def Astar(T):
    Star = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for x in range(0, 3):
        for y in range(0, 3):
            Star[x][y]=det2M(x,y,T)
            if(x+y)%2!=0:
                Star[x][y]=Star[x][y]*-1
    return Star

def Aminus(M,d):
    for x in range(0,3):
        for y in range(0,3):
            if M[x][y]!=0:
                M[x][y]=M[x][y]/d
    return M

def AminusB():
    X[0][0]=AI[0][0]*B[0][0]+AI[0][1]*B[1][0]+AI[0][2]*B[2][0]
    X[1][0]=AI[1][0]*B[0][0]+AI[1][1]*B[1][0]+AI[1][2]*B[2][0]
    X[2][0] = AI[2][0] * B[0][0] + AI[2][1] * B[1][0] + AI[2][2] * B[2][0]

def citire():
    with open("tema1.txt", 'r') as reader:
        sir = reader.readline()
        line=0
        pozitiv=1
        nur=0
        while sir:
            print(sir)
            for character in sir:
                if"0"<=character and character<="9":
                    nur=nur*10+(ord(character)-ord("0"))
                elif character=="-":
                    pozitiv=-1
                elif character=="x":
                    if nur==0:
                        nur=1
                    A[line][0]=nur*pozitiv
                    pozitiv = 1
                    nur = 0
                elif character == "y":
                    if nur==0:
                        nur=1
                    A[line][1] = nur * pozitiv
                    pozitiv = 1
                    nur = 0
                elif character=="z":
                    if nur==0:
                        nur=1
                    A[line][2]=nur*pozitiv
                    pozitiv = 1
                    nur = 0
            B[line][0]=nur*pozitiv
            line=line+1
            nur=0
            pozitiv=1
            sir = reader.readline()

citire()
print(A)
print(B)
print("----------incepe rezolvarea-----------")
determinantA=det3(A)
print(determinantA)
if(determinantA!=0):
    AT=transpusa(A)
    print(AT)
    AS=Astar(AT)
    print(AS)
    AI=Aminus(AS,determinantA)
    print(AI)
    AminusB()
    print(X)
    print("----------gata rezolvarea-----------")
else:
    print("determinantul e 0, deci nu se poate continua rezolvarea")
    print("----------intrerupem rezolvarea-----------")

import numpy as np

m1 = np.array([[0,0,0],[0,0,0]])


