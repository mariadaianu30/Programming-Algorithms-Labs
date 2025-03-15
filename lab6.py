# Link pentru laborator: https://docs.google.com/document/d/1bU5Srecwv9WjE3aD7TnxATIauHr582qZ/edit?usp=sharing&ouid=103396152483260729031&rtpof=true&sd=true

#problema 1 

# L=[int(x) for x in input("lista: ").split()]

#a)
# print(sorted(L, key=str))

#b)

# print(sorted(L, key=lambda x: str(x)[::-1]))

#c)
# print(sorted(L,key=lambda x: len(str(x))))

#d)
# print(sorted(L,key=lambda x: len(set(str(x)))))

#e)
# print(sorted(L, key=lambda x: (len(str(x)), -x)))

#f)
# print(sorted(L, key=lambda x: ( -x if x % 2 == 0 else x)))

#g)
# sir="Se citește o propoziție cu cuvinte separate prin spațiu"
# cuv=sir.split()

# cuv=sorted(cuv, key=lambda x:-len(x))
# print(" ".join([str(x) for x in cuv ]))

#h)
# l=[int(x) for x in input("lista: ").split()]

# print(sorted(l, key=lambda x: (sum([int(c) for c in str(x)]),-x)))

#problema 2
# d={}
# f=open("input.txt")
# for line in f:
#     cnp, nume, prenume, note = line.split(maxsplit=3)
#     cnp=int(cnp)
#     list_note=[int(x) for x in note.split()]
#     d[cnp]=[nume,prenume,list_note]
# f.close()

#b)
# def creste_nota(cnp,d):

#     if cnp not in d:
#         return None
    
#     if d[cnp][2][0]<10:
#         d[cnp][2][0]+=1

#     return d[cnp][2][0]

# cnp1=int(input("cnp-ul este : "))
# print(creste_nota(cnp1,d))
# print(d)

#c)
# def notes(cnp,lista_note,d):
    
#     if cnp not in d:
#         return None
#     d[cnp][2].extend(lista_note)

#     return d[cnp][2]
# cnp1=int(input("cnp: "))
# lista_note=[int(x) for x in input("notele adaugate sunt:").split()]
# print(notes(cnp1,lista_note,d))
# print(d)
    
#d)

# def delete(cnp,d):
#     if cnp not in d:
#         return None
#     del d[cnp]
# cnp1=int(input("cnp: "))
# delete(cnp1,d)
# print(d)

#e)
# import string
# import random

# def genereaza_coduri(d):
#     for cnp in d:
#         cod = "".join(random.choices(string.ascii_letters , k=3) +
#                       random.choices("0123456789", k=3))
#         d[cnp].append(cod)
# genereaza_coduri(d)
# print(d)

#problema 3
# f=open("input.txt", "r")
# cuv_list=f.read().split()
# f.close()

# p=int(input("p="))
# d={}

# for cuv in cuv_list:
#     if cuv[-p:] not in d:       #verifica daca ultimele p litere ale unui cuvant sunt in dictionar
#         d[cuv[-p:]]=[cuv]       #daca nu, le initializeaza ca si key element si ii atribuie cuvantul curent ca valoare
#     else:
#         d[cuv[-p:]].append(cuv)     #daca exista cheia formata din ultimele p cifre , adauga elementul la values
# rez=sorted(d.values(), key=lambda L: -len(L))       #sorteaza valorile in functie de lungime

# with open("output.txt", "w") as g:
#     for l in rez:
#         g.write(" ".join(sorted(l,reverse=True)) +"\n")     #sortare in ordine alfabetica
# g.close()

#problema 4
# f=open("input.txt", "r")
# l_cuv=f.read().split()

# f.close()

# d={}

# for cuv in l_cuv:
#     litere=frozenset(cuv)
#     if litere not in d:
#         d[litere]=[cuv]
#     else:
#         d[litere].append(cuv)
# rez=[sorted(l_cuv, key=len) for litere, l_cuv in sorted(d.items(), key=lambda t: -len(t[0])) if len(l_cuv)>=2]


# print(rez)

#problema 6

# import random
# import string

# # Funcția care generează parola aleatorie
# def genereaza_parola():
#     # Generăm o literă mare
#     mare = random.choice(string.ascii_uppercase)
#     # Generăm 3 litere mici
#     mici = random.choices(string.ascii_lowercase, k=3)
#     # Generăm 4 cifre
#     cifre = random.choices(string.digits, k=4)
    
#     # Combinăm și formăm parola
#     parola = mare + ''.join(mici) + ''.join(cifre)
#     return parola

# # Citim datele din fișierul "date.in"
# with open("input.txt", "r") as f:
#     studenti = f.readlines()

# # Creăm lista de conturi și parole
# rezultate = []

# for student in studenti:
#     # Eliminăm spațiile inutile și împărțim numele și prenumele
#     student = student.strip()
#     nume, prenume = student.split()
    
#     # Generăm contul de email
#     email = f"{prenume.lower()}.{nume.lower()}@s.unibuc.ro"
    
#     # Generăm parola
#     parola = genereaza_parola()
    
#     # Adăugăm rezultatul în listă
#     rezultate.append(f"{email},{parola}")

# # Scriem rezultatele în fișierul "date.out"
# with open("output.txt", "w") as f:
#     for rezultat in rezultate:
#         f.write(rezultat + "\n")
