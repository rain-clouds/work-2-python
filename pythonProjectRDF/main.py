import string

from rdflib import Graph,Literal,URIRef
from rdflib.namespace import RDF, RDFS, OWL, FOAF, XSD
#punem in graf elementele din ontologie
g = Graph()
g.parse('D:\pls mergi.owl')
#folosim un ok ca sa vedem daca gasim cuvantul dorit
ok = 0
#citim cuvantul
x = input()
#avem nevoie de o variabila care sa retina conceptul asociat cuvantului gasit
i1=None
#cautam cuvantul intre subiecti- care sunt conceptele si obiecte care pot fi si literali(adica chiar cuvantul de care avem nevoie)
for s, o in g.subject_objects(RDFS.label):
    #am gasit cuvantul
     if(o.value==x):
          print(s,o)
          ok=1
          i1=s
         #in general e unul singur, asa ca nu avem nevoie sa parcurgem chiar tot graful
          break
#daca am gasit cuvatul asociat conceptului

if ok==1:
    #afisam conceptul
    print(i1)
    #cautam toate relatiile in care conceptul e obiect, numai de siguranta, sa fim siguri ca ia toate relatiile asociate cu conceptul, in care acest concept e obiect, adica relatia se rasfrange asupra lui
    for s,p,o in g.triples((None,None,i1)):
        print(s,p)
    print()
    print()
    #cautam specific relatiile superTopic Of, cu ajutorul uriref-ului
    for s,p,o in g.triples((None,URIRef("http://cso.kmi.open.ac.uk/schema/cso#superTopicOf"),i1)):
        print(s)
#nu facem toate aceste operatii daca am introdus un cuvant care nu apartine ontologiei
else: print("nu exista")



