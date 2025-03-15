#Link pentru laborator: https://docs.google.com/document/d/1WM1XypigbW_tepXfieslSPZ2uM5FdRN9l-wJc5LWIWo/edit?usp=drive_link

#problema 1

#varianta 1

# f=open("input.txt", "r")
# file=f.read()
# f.close()

# g=open("output.txt", "w")
# g.write(file)
# g.close()

#varianta 2

# f=open("input.txt","r")
# g=open("output.txt", "w")

# while True:
#     line=f.readline()
#     if line=="":
#         f.close()
#         g.close()
#         break
#     g.write(line)

#varianta 3

# with open("input.txt") as f:
#     L_linii=f.readlines()
# with open("output.txt", "w") as g:
#     g.write("".join(L_linii))


#problema 2

# f=open("input.txt")
# g=open("output.txt","w")
# nota=0

# for line in f:
#     prod,rez=line.split("=")
#     a,b=prod.split("*")
#     a,b,rez=int(a), int(b), int(rez)

#     produs=a*b
#     if produs==rez:
#         nota+=1
#         g.write(f"{line.strip()} Corect\n")
#     else:
#         g.write(f"{line.strip()} Gresit\n")
# g.write(f"Nota finala este {nota}")

#problema 3

# m,n=[int(x) for x in input("m,n:").split()]
# matrix=[[int(x) for x in input(f"linia{i}:").split()] for i in range(m)]

# L_max=[max(line) for line in matrix]
# print(L_max)


#problema 4
# m,n=[int(x) for x in input("m,n:").split()]
# matrix=[[int(x) for x in input(f"linia{i}").split()] for i in range(m)]
# k=int(input("k="))

#varianta 1
# matrix[k+1:k+1]=[[0]*n]         #pentru ca limitele slice-ului sunt egale, atunci se va insera o linie noua pe pozitita k+1
# print(*matrix, sep='\n')

#varianta 2

# matrix.insert(k+1, [0]*n)       #insereaza o noua lista la linia k+1
# print(*matrix, sep="\n")


#problema 5

# f=open("input.txt")
# matrix=[[int(x) for x in line.split()] for line in f]       #matrice
# f.close()

# L_produse=[eval("*".join(str(x) for x in line)) for line in matrix]     #eval are rolul de a evalua matematic o expresie

# rez=L_produse.count(max(L_produse))
# print(rez)

#problema 6

# f=open("input.txt")
# matrix=[[int(x) for x in line.split()] for line in f]
# f.close()

# n=len(matrix[0])

# k=int(input("n="))

# for i in range(n):
#     matrix[i]=matrix[i][-k:]+matrix[i][:-k]
#             #ultimele el din matrice
# with open("output.txt", "w") as g:
#     g.write("\n".join([' '.join(str(x) for x in line) for line in matrix]))

#problema 7
#subpunctul a 
# m,n=[int(x) for x in input("m,n:").split()]
# matrix=[[int(x) for x in input(f"line{i}: ").split()] for i in range(m)]

# lcol=len(matrix[0])
# llinii=len(matrix)

# transpusa=[[matrix[i][j] for i in range(lcol)] for j in range(llinii)]

# print('\n'.join([" ".join(str(x) for x in line) for line in transpusa]))

#subpunctul b
# f=open("input.txt")
# matrix=[[int(x) for x in line.split()] for line in f]
# nr_col=len(matrix[0])
# nr_linii=len(matrix)

# transpusa=[[matrix[i][j] for i in range(nr_linii)] for j in range(nr_col)]

# with open("output.txt", "w") as g:
#     g.write('\n'.join([" ".join(str(x) for x in line) for line in transpusa]))
# g.close()

# #problema 8

# m,n=[int(x) for x in input(f"m,n: ").split()]
# matrix=[[int(x) for x in input(f"line {i}: ").split()] for i in range(m)]
# pare=0
# for line in matrix:
#     for i in line:
#         if i%2==0:
#             pare+=1
# print(pare)


#problema 9

# m,n=[int(x) for x in input(f"m,n: ").split()]
# matrix=[[int(x) for x in input(f"line {i}: ").split()] for i in range(m)]
# l=[]
# for line in matrix:
#     sum=0
#     minim=1000000000
#     for i in line:
#         sum+=i
#     for i in line:
#         if sum-i <minim:
#             minim=sum-i
#     l.append(minim)

# print(l)

#problema 10
# m,n=[int(x) for x in input("m,n:").split()]
# matrix=[[int(x) for x in input(f"line {i}: ").split()] for i in range(m)]
# #daca codul liniei e par atunci se afiseaza de la dreapta la stanga, daca nu se afiseaza de la stanga la dreapta

# for i in range(len(matrix)):
#     if i%2==0:
#         print(*matrix[i])
#     else:
#         print(*matrix[i][::-1])

#problema 11
# m,n=[int(x) for x in input("m,n:").split()]
# matrix=[[int(x) for x in input(f"line {i}: ").split()] for i in range(m)]
# count=0
# for line in matrix:
#     for i in line:
#         if i<0:
#             count+=1
# print(count)

#problema 12
# m,n=[int(x) for x in input("m,n:").split()]
# matrix=[[int(x) for x in input(f"line {i}: ").split()] for i in range(m)]
# nr=len(matrix)
# print(nr)
# for line in matrix:
#     for i in line:
#         if i!=line[0]:
#             nr-=1
#             break
# print(f"Numarul de linii care au toate elementele egale este {nr}")


#problema 14

# def Fibonacci_lastdigit(n):
#     if n <= 1:
#         return n
#     a, b = 0, 1
#     for _ in range(2, n + 1):
#         a, b = b, (a + b) % 10  # Calculăm doar ultima cifră
#     return b


# n=int(input("n="))
# matrix=[]
# for i in range(n):
#     row=[]
#     for j in range(1,n+1):
#         index=n*i+j
#         row.append(Fibonacci_lastdigit(index))
#     matrix.append(row)

# print ("\n".join([' '.join(str(x) for x in line) for line in matrix]))

#problema 15

# n=int(input("n="))
# matrix=[[int(x) for x in input(f" line {i}: ").split()] for i in range(n)]
# l=[]
# for i in range(n):
#     for j in range(n):
#         if i>j and i+j >n-1:
#             l.append(matrix[i][j])

# s=set(l)
# print(s)

#problema 16

# f=open("input.txt")
# matrix=[[int(x) for x in line.split()] for line in f]
# nr_col=len(matrix[0])
# nr_linii=len(matrix)

# transpusa=[[matrix[i][j] for i in range(nr_col-1,-1,-1)] for j in range(nr_linii)]

# with open("output.txt", "w") as g:
#      g.write('\n'.join([" ".join(str(x) for x in line) for line in transpusa]))
# g.close()

#problema 12
