#link pentru laborator: https://docs.google.com/document/d/1mLMT0GV-k1mkHyDnn1rPTAadoa6Qc0DtWCD1d7NEJ-s/edit?usp=drive_link

#problema 1

# n=int(input("n="))

# x=n
# inv=0
# while x:
#     inv=inv*10+x%10
#     x=x//10

# if n!=inv:
#     print("numarul nu e palindrom")
# else:
#     print("numarul e palindrom")

#problema 2
# import math

# L1=int(input("L1="))
# L2=int(input("L2="))

# gcd=math.gcd(L1,L2)


# print(f"avem nevoie de {(L1*L2)//(gcd*gcd)} de placi  de dimensiune {gcd}")

#problema 3

# start=int(input("start: "))
# stop=int(input("stop: "))

# x=1
# y=1
# z=1

# while z<start:
#     z=y+x
#     x=y
#     y=z
# if z<= stop:
#     print(f"cel mai mic numar fibonacci din [{start},{stop}] este {z} ")

#problema 4

# a=int(input("a="))
# b=int(input("b="))

# for i in range(0,100,5):
#     if i not in range (a,b+1):
#         print(i, end=" ")
# print()
# for i in range(-99,-1,5):
#     if i not in range (a, b+1)
#     print(i, end=" ")
#problema 5

# n=int(input("n="))
# x=0
# for i in range(1,n+1):
#     x+=1
#     for j in range(1,x+1):
#         print(j, end=" ")
#     print()


#problema 6

# n=input("n=")
# nrmin=""
# nrmax=""
# fr={}
# for c in n:
#     if c in fr:
#         fr[c]+=1
#     else:
#         fr[c]=1

# for cif in range(1,10):
#     if str(cif) in fr:
#         nrmin+=str(cif)
#     if str(cif) in fr:
#         nrmin+=str(cif)
#         fr[str(cif)]-= 1
#         break
# for i in range (0,10):
#     if str(i) in fr:
#         nrmin+=str(i)*fr[str(i)]
# for i in range(9,-1,-1):
#     if str(i) in fr:
#         nrmax += str(i) * fr[str(i)]

# print(f"numarul minim este {nrmin}")
# print(f"numarul maxim este {nrmax}")

#problema 7

# n=int(input("n="))
# list=[]
# ap=0
# sir=[int(x) for x in input().split()]
#sir =list(map(int,input().split()))

# for _ in range(n):
#     x=input("x=")
#     list.append(x)

# minim=min(list)

# for i in list:
#     if i==minim:
#         ap+=1
# print(f"numarul de aparitii al nr minim {minim} este {ap}")

#problema 8

# n=int(input("n="))
# list=[]
# max1=max2=0
# for i in range(n):
#     list.append(int(input("i=")))

# for j in list:
#     if j>max1:
#         max2=max1
#         max1=j
        
#     elif j>max2:
#         max2=j

# print(f"cele 2 maxime sunt {max1} si {max2}")

#problema 9

# import math
# a=int(input("a="))
# b=int(input("b="))

# for i in range(a,b+1):
#     if math.log(i,2)==int(math.log(i,2)):
#         print(i, end=" ")

#problema 10

# n=int(input("n="))
# a=int(input("Cap interval stanga: "))
# b=int(input("Cap interval dreapta: "))
# for i in range(2, n+1):
#     x=int(input(f"Cap interval stanga {i}: "))
#     y=int(input(f"Cap interval dreapta {i}: "))
#     a,b=max(a,x),min(b,y)
#     if a>=b:
#         print("Studentii nu pot fi simultan prezenti")
#         break
#     else:
#         print(f"Studentii sunt simultan prezenti in intervalul [{a}, {b}]")

#problema 11

# n=int(input("n="))
# array=[]
# ok=True
# for x in range(n):
#     array.append(int(input("x=")))

# maxim=max(array)
# poz=array.index(maxim)

# print(poz)

# for i in range(poz):
#     if array[i]>array[i+1]:
#         ok=False
# for i in range(poz, n-1):
#     if array[i]<array[i+1]:
#         ok=False
# if ok:
#     print("vectorul este creasta")
# else:
#     print("vectorul nu este creasta")

#problema 12

# n=input("n=")
# s=0
# for c in n:
#     s+=int(c)
# print(s)
# s1=s
# s=0
# while s1!=0:
#     s=s+s1%10
#     s1=s1//10
#     if s>=10:
#         s1=s
#         s=0
# print(s)
        
#problema 13
# n=int(input("n="))

# while n>1:
#     print(n, end=" ")
#     if n%2==0:
#         n=n-1
#     else:
#         n=n//2+1

# print(1)

#problema 14

# n=int(input("n="))
# nr=2

# for i in range(2,n//2+1):
#     if(n%i==0):
#         nr=nr+1
# print(f"numarul de divizori este {nr}")

#problema 15

# n=int(input("n="))
# maxdiv=2
# minim=0
# for i in range(n,0,-1):
#     nrdiv=2
#     for j in range (2,n):
#         if(i%j==0):
#             nrdiv+=1
#     if nrdiv>=maxdiv:
#         maxdiv=nrdiv
#         minim=i
    
# print(minim)

#problema 16

# n=int(input("n="))
# nrdiv=0
# for div in range(1,n+1):
#     if(n%div==0):
#         nrdiv+=1
# if nrdiv==3:
#     print(f"true")
# else:
#     print("false")

#problema 17
# a=int(input("a="))
# b=int(input("b="))
# nrdiv=0
# for i in range(1,b+1):
#     if a%i==0 and b%i==0:
#         nrdiv+=1

# print(f"numarul de divizori comuni este {nrdiv}")

#problema 18
# n=int(input("n=")) 
# m=n
# nrzerouri=0

# while n>=5:
#     if n%5==0:
#         nrzerouri+=n//5
#     n=n//5
# print(f"se gasesc {nrzerouri} de zerouri in {m}! ")

#problema 19

# n=int(input("n="))
# if n == 0:
#      print(1)

# total = 10  # Numerele de o cifră: 0-9
# produs = 9  # Pentru cifre unice în numere mai mari
# cifre = 9

# for i in range(2, n + 1):
#     produs *= cifre
#     total += produs
#     cifre -= 1
# print(total)
