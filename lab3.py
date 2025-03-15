#Link pentru laborator: https://docs.google.com/document/d/1a0Mtr6Zt5TV30k5E0niEIJv8S_9VY81QDRBv9uLDRxg/edit?usp=sharing

#problema 2
# s = input("Introdu un sir de caractere: ")
# for i in range(len(s) // 2 + len(s) % 2):
#     print(s[i: len(s) - i].center(len(s), " "))

#problema 3

# s=input("sirul de caractere este: ")
# t=input("subsirul este: ")
# if s.find(t)!=-1:
#     print(f"{t} este subsir al lui {s}")
# else:
#     print(f"{t} nu este subsir in {s}")

# # metoda find cauta si returneaza prima aparitiei a subsirului in sirul principal. in cazul in care nu gaseste subsirul in sirul dat, returneaza -1
# poz=s.find(t)
# while poz!=-1:
#     print(poz, end=" ")
#     poz=s.find(t, poz+len(t))


#problema 4
# propozitie=input("propozitia este:")
# s=input("sirul corect este:")
# t=input("sirul gresit este: ")
# prop2=propozitie
# propozitie=propozitie.replace(t,s)
# print(f"propozitia corecta este:  {propozitie}")

# p=int(input("numarul maxim de corectari: "))

# prop2=prop2.replace(t,s,p)
# if(prop2!=propozitie):
   
#     print(f"testul contine prea multe greseli, doar {p} au fost corectate, propozitia corectata este {prop2}")
# else:
#     print(f"propozitia corecta este:  {prop2}")

#problema 5
# sentence=input("the sentence is:")
# s=input("the word that is replaced:")
# t=input("the word we replace it with: ")

# words=sentence.split()
# new_sentence=" ".join([ t if word==s else word  for word in words])
# print(f" the new sentence is:  {new_sentence}")

#problema 6

#a) Encode- Caesar's Code

# text=input("textul este: ")
# k=int(input())
# rezultat=[]
# for x in text:
#     if x.isalpha():
#         if x.isupper():
#             charshift=chr((ord(x)-65+k)%26+65)
#         else:
#             charshift=chr((ord(x)-97+k)%26+97)
#         rezultat.append(charshift)
#     else:
#         rezultat.append(x)
# print(f"sirul criptat este {"".join(rezultat)}")

# #b ) Decode- Caesar's Code

# text=input("textul este: ")
# k=int(input())
# rezultat=[]
# for x in text:
#     if x.isalpha():
#         if x.isupper():
#             charshift=chr((ord(x)-65-k)%26+65)
#         else:
#             charshift=chr((ord(x)-97-k)%26+97)
#         rezultat.append(charshift)
#     else:
#         rezultat.append(x)
# print(f"sirul decriptat este {"".join(rezultat)}")

#problema 7- Limba pasareasca 

# text=input("textul este: ")
# vocale="aeiouAEIOU"

# rezultat=""

# for char in text:
#     rezultat+=char
#     if char in vocale:
#         rezultat+='p'
#         rezultat+=char.lower() 
# print(rezultat)


#problema 8

# phrase=input("fraza din jurnalul Anei este: ")
# s=0
# list=phrase.split(" ")
# for cuv in list:
#     if cuv.isnumeric():
#         s+=int(cuv)
# print(s)

#problema 9   -acronim

# text=input("text: ")
# acronim=""

# if text[0].isupper():
#     acronim+=text[0]
# i=1
# while i<len(text):
#     if text[i].isupper() and text[i-1]==' ':
#         acronim+=text[i]
#     i+=1
# print(f"acronimul este {acronim}")


#problema 10

# a=input("primul text este: ")
# b=input("al doilea text este: ")
# sablon=""
# vocale="aeiouAEIOU"
# if len(a)!=len(b):
#     print("nu se poate construi sablonul")
# i=0
# while i<len(a):
#     if a[i] in vocale and b[i] in vocale:
#         sablon+='*'
#     elif a[i] not in vocale and b[i] not in vocale:
#         sablon+='#'
#     else:
#         sablon+='?'
#     i+=1

# print(f"sablonul pentru sirurile {a} si {b} este {sablon}")

#problema 11
# def palindrom(s):
#     ok=True
#     t=s
#     s=s[::-1]
#     if t==s:
#         ok=True
#     else:
#         ok=False
#     return ok

# word=input("word:")

# prefix=""
# sufix=""
# maxs=maxf=0

# for i in word:
#     prefix+=i
#     if palindrom(prefix) and len(prefix)>maxf:
#         maxf=len(prefix)
#         prefixbun=prefix

# for i in word[::-1]:
#     sufix+=i
#     if palindrom(sufix) and len(sufix)>maxs:
#         maxs=len(sufix)
#         sufixbun=sufix
# print(f"prefixul de lungime maxima este: {prefixbun} , iar sufixul este: {sufixbun}")

#problema 12

# text=input("textul este:")

# maxim=0
# words=text.split(" ")
# final=""
# print(words)
# for cuv in words:
#     print(cuv[::-1])
#     if len(cuv)>maxim:
#         maxim=len(cuv)

# for cuv in words:
#     if len(cuv)==maxim:
#         final+=cuv[::-1]
#         final+= ' '
#     else:
#         final+=cuv
#         final+= ' '
# print(final.strip())

#problema 13

# text=input("text:")
# baza=0
# for i in range(len(text)):
#     baza+=26**i*(ord(text[len(text)-i-1])-97)

# print(baza)

#problema 14

# text=input("text:")
# list=text.split(" ")
# length=maxim=0
# rezultat=""
# cleaned_list=[word for word in list if word.strip()]  #!!!!!!!!!  

# value=cleaned_list[0][len(cleaned_list[0])-1]
# rezultat="".join(cleaned_list[0])

# for word in cleaned_list[1::]:
#     if value==word[0]:
#         rezultat="".join(word)
#         value=word[len(word)-1]
#     else:
#         print(rezultat)
#         rezultat=""

