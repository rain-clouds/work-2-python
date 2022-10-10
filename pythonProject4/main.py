

# Joc: (generalizare Mastermind) Jucătorul A are bile de n culori diferite, câte m bile de fiecare culoare. Jucătorul A alege k bile, fără ca alegerea să fie vizibilă pentru jucătorul B. Un pas al jocului constă în:
# Jucătorul B propune o secvență de k  culori. O culoare se poate repeta de cel mult m ori.
# Jucătorul A indică o valoare între 0 și k corespunzătoare numărului de potriviri de culori și poziții între secvența propusă de B și bilele alese la începutul jocului.
# Dacă după cel mult 2*n pași jucătorul B a propus secvența de culori corespunzătoare secvenței de k bile alese de jucătorul A, jucătorul B câștigă jocul. Altfel, câștigă jucătorul A.
#
# Demo online pentru n=8, k= 4,6 sau 8 care include și indicarea culorii corecte fără a fi și poziția corectă (cerință care nu e inclusă mai sus): https://www.webgamesonline.com/mastermind/index.php
#
# Etape de rezolvare:
# (0.2) Implementați funcția de inițializare (primește ca parametrii n, m și k, întoarce starea inițială) și funcția care verifică dacă o stare primită ca parametru este finală, caz în care întoarce câștigătorul.
# (0.2) Implementați o funcție care alege aleator k bile din cele m*n disponibile.



def initializare(n,m,k):
    #primim nr de culori , nr de bile, ne de repetari a unei bile si lasam jucatorul A sa aleaga
    aparitii=[0 for i in range(n)]
    stare_initiala=[-1 for i in range(k)]
    for i in range(0,k):
        x=int(input())
        while True:
            ok=1
            if x<0 or x>=n:
                print("alegeti un numar intre 0 si ",n)
                ok=0
            elif (aparitii[x]>=n):
                print("alegeti un numar intre 0 si ", n, "care nu a atins geadul maxim de utilizare")
            else: break
            x = int(input())

        print(x)
        aparitii[x]+=1
        stare_initiala[i]=x
    return (stare_initiala)




final_form=initializare(8,3,5)
print (final_form)


def verificare(stare_curenta,nr_guesses,total_guesses):
     if(nr_guesses<=total_guesses*2):
        return stare_curenta==final_form #nr de fhiciri <=2*n



import random

def alege_random(n,m,k):
    aparitii = [0 for i in range(n)]
    stare_random = [-1 for i in range (k)]
    i=0
    while i<k:
        x=random.randint(0,n)
        if(aparitii[x]<m):
            aparitii[x]+=1
            stare_random[i]=x
            i+=1
    return(stare_random)

random_state=alege_random(8,3,5)

print(random_state)

