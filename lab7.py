# Link pentru laborator: https://docs.google.com/document/d/1fRHKC3FIxMhKwYFF7TdcjmFs46-YHIzz/edit?usp=sharing&ouid=103396152483260729031&rtpof=true&sd=true

#problema 2

#a)
# def nr_max(*nr):
#     cif_max=[]
#     for n in nr:
#         cif_max.append(max(str(n)))
#     cif_max.sort(reverse=True)

#     return int("".join(x for x in cif_max))

# # print(nr_max(34,58,99,102))     

# #b)
# def baza_doi(a,b,c):
#     for i in str(a):
#         if i not in ('0','1'):
#             return False
    
#     for i in str(b):
#         if i not in ('0','1'):
#             return False
    
#     for i in str(c):
#         if i not in ('0','1'):
#             return False    

#     return True
    
# a=int(input("a= "))
# b=int(input("b="))
# c=int(input("c= "))
# print(baza_doi(a,b,c))

#problema 3

#
# def cautare_cuvant(cuv, nume_fis_out, *nume_fis_in):
#     cuv = cuv.lower()
#     with open(nume_fis_out, "w") as g:
#         for nume in nume_fis_in:
#             with open(nume) as f:
#                 L = []  # indexi liniilor
#                 for i, linie in enumerate(f):
#                     L_cuv = [c.strip("!?.,;:")
#                             for c in linie.lower().replace('-', ' ').split()]
#                     if cuv in L_cuv:
#                         L.append(i + 1)
#                 g.write(f"{nume} {"Cuvantul nu a fost gasit" if len(L) == 0
#                 else " ".join([str(x) for x in L])}\n")


# cautare_cuvant("fLoaRe","rez.txt", "eminescu.txt", "paunescu.txt")
# cautare_cuvant("alBastRa", "rez.txt", "eminescu.txt", "paunescu.txt")
