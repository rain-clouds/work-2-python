import random

def initializare(n,m,k):
    #primim nr de culori , nr de bile, nr de repetari a unei bile si lasam jucatorul A sa aleaga
    #initializam numarul de aparitii si vectorul de stare initiala
    aparitii=[0 for i in range(n)]
    stare_initiala=[-1 for i in range(k)]
    for i in range(0,k):
        #formam vectorul si permitem doar optiuni valide
        x=int(input())
        while True:
            if x<0 or x>=n:
                print("Alegeti un numar intre 0 si",n-1,".")
                ok=0
            elif (aparitii[x]>=m):
                print("Alegeti un numar intre 0 si",n-1,"care nu a atins gradul maxim de utilizare.")
            else: break
            x = int(input())

        print(x)
        aparitii[x]+=1
        stare_initiala[i]=x
    return (stare_initiala)


#luam starea curenta, cea finala si numarul de inercari si vedem daca jucatorul a ghicit corect
def verificare(stare_curenta,nr_guesses,total_guesses,final_form):
     if(nr_guesses<=total_guesses*2):
        return stare_curenta==final_form #nr de ghiciri <=2*n
     return False


#genereaza un sir radom intr-un range dat
def alege_random(n,m,k):
    aparitii = [0 for i in range(n)]
    stare_random = [-1 for i in range (k)]
    i=0
    while i<k:
        x=random.randint(0,n-1)
        while True:
            if(aparitii[x]<m):
                aparitii[x]+=1
                stare_random[i]=x
                i+=1
                break
            else: x=random.randint(0,n-1)
    return(stare_random)


#luam cele 2 secvente si comparam pozitie cu pozitie
def potriviri(current_state,final_form,k):
    ap=0
    for i in range(k):
        if current_state[i]==final_form[i]:
           # print("pozitia " i " s-a potrivit")
            ap+=1
    return ap

def player_B(n,m,k):
    A=alege_random(n,m,k)
    print("A:",A)
    print("Jucatorul B poate incepe sa ghiceasca. Indicele culorilor pe care le poate alege sunt intre 0 si",n-1,".")
    print("Nu uitati sa dati enter dupa ce ati ales o culoare.")
    print("Atentie, Nu puteti reveni sa modificati o culoare culoare introdusa anterior dupa ce ati apasat enter")
    gata=0
    #simuleaza rundele prin care jucatorul b trebuie sa treaca
    for i in range(2*n):
        print("mai aveti ", 2*n-i ," incercari")
        #inregistreaza alegerile facute de jucatorul B
        B=initializare(n,m,k)
        #verifica daca B a ajuns la decizia corecta
        if verificare(B,i,2*n,A):
            print("Jucatorul B a castigat!")
            gata=1
            break
        else:
            #verifica numarul de potriviri
            p=potriviri(B,A,k)
            print("Jocul continua! Au fost ",p," potriviri.")
            print("B:",B)
            print("A:",A)
            print()
            print("Introdueti culorile")
            print()

    #daca B nu a reusut sa ghiceasca pana la final, a pierdut
    if gata==0:
        print("Jucatoarul A a castigat!")

    print(A)
print()
print()
print("Pentru ca e posibil sa avem multe culori, o sa notam culorile de la 0 la nr de culori-1")
print()
print("introduceti numarul de culori")
a=int(input())
print("introduceti de cate ori se poate repeta o culoare")
b=int(input())
print("introduceti cate culori vreti sa selectati pentru puzzle")
c=int(input())
print("sa inceapa jocul")

player_B(a,b,c)