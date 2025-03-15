# link pentru laborator: https://docs.google.com/document/d/1wCK2Vu7Ny4js_ahzIdDdL9UL-g9gwegY/edit?usp=sharing&ouid=103396152483260729031&rtpof=true&sd=true



#problema 1

# x=int(input("x="))
# y=int(input("y="))

# print(x+y, x*y)
# print(x+y, x*y, sep="\n")
# print(f"suma numerelor {x} si {y} este {x+y}, iar produsul este {x*y}")

#problema 2

# x=int(input("x="))
# y=int(input("y="))
# z=int(input("z="))

# if 0<=x<24 and 0<=y<60 and 0<=z<60:
#     print(f"{x:02d}:{y:02d}:{z:02d}")
# else:
#     print("numerele nu pot reprezenta ore, minute sau secunde")

#problema 3

# z=int(input("z="))
# l=int(input("l="))
# a=int(input("a="))
# ok=True

# if l in [1,3,5,7,8,10,12]:
#     #luna cu 31 de zile
#     if 1<=z<31:
#         z+=1
#     elif z==31:
#         z=1
#         if l==12:
#             l=1
#             a+=1
#         else:
#             l+=1
#     else:
#         ok=False

# if l in [4,5,9,11]:
#     #luni cu 30 de zile
#     if 1<=z<30:
#         z+=1
#     elif z==30:
#         z=1
#         l+=1
#     else:
#         ok=False

# if l==2:
#     if (a%4==0 and a%100!=0) or (a%400==0):
#         if 1<=z<29:
#             z+=1
#         elif z==29:
#             z=1
#             l+=1
#         else:
#             ok=False

#     else:
#         if 1<=z<28:
#             z+=1
#         elif z==28:
#             z=1
#             l+=1
         
#         else:
#             ok=False

# else:
#     ok=False   

# print(f"{z:02d}.{l:02d}.{a:04d}")


#pb 4
# x=int(input("x="))
# y=int(input("y="))
# op=input("op=")

# if op in "*/-+":
#     if op=='+':
#         r=x+y
#     if op=='/':
#         r=x/y
#     if op=='-':
#         r=x-y
#     if op=='*':
#         r=x*y
#     print(f"rezultatul este {r:3f}")
# else:
#     print("nu exista op")


#pb 5
# valori=input("date citite de la tastatura:").split()
# int1=int(valori[0])
# int2=int(valori[1])
# float1=float(valori[2])
# float2=float(valori[3])
# char1=valori[4]
# char2=valori[5]

# #1
# print(int1,int2,float1,float2,char1,char2)

# #2
# print(int1,float1,char1,int2, float2, char2)

# #3
# print(int1)
# print(int2)
# print(float1)
# print(float2)
# print(char1)
# print(char2)

#pb 6
# n= int(input("n="))
# cursurival=list(map(float,input(f"cursuri valutare pe zile: ").split()))

# if(len(cursurival)!=n):
#     print("eroare")

# maxim=zi1=zi2=0
# for i in range(1,n):
#     dif=cursurival[i]-cursurival[i-1]
#     if dif>maxim:
#         maxim=dif
#         zi1=i
#         zi2=i+1
# print(f"diferenta maxima este de {maxim:.2f}in zilele {zi1} si {zi2}")

#problema 8

# x=int(input("x="))
# y=int(input("y="))
# z=int(input("z="))

# maxim=max(x,y,z)
# minim=min(x,y,z)

# print(maxim-put("y="))minim)

#problema 9

# x=int(input("x="))
# y=int(input("y="))
# z=int(input("z="))

# if x<y:
#     if y<z:
#         print(f"{x}<{y}<{z}")
#     else:
#         if x<z:
#             print(f"{x}<{z}<{y}")
#         else:
#             print(f"{z}<{x}<{y}")
# elif x>y:
#     if y<z:
#         if x<z:
#             print(f"{y}<{x}<{z}")
#         else:
#             print(f"{y}<{z}<{x}")

    # else:
    #     print(f"{z}<{y}<{x}")


        