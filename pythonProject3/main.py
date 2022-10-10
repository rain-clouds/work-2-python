import numpy as np

A= np.array([[0,0,0],[0,0,0],[0,0,0]])
B= np.array([[0],[0],[0]])
print(A)
print(B)

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
AI=np.linalg.inv(A)
print(AI)
X=np.matmul(AI,B)
print(X)
