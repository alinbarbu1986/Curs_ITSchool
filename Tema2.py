'''Problema 1. Se citeste de la tastatura o parola. Sa se verifice daca parola introdusa are
    cel putin 10 caractere si nu contine spatiu.
Sa se afiseze un mesaj corespunzator pentru fiecare neregula gasita
    sau mesajul "OK" in cazul in care parola respecta regulile.
    hints: boolean, conditionals'''

'''parola = input('Introdu parola: ')

if len(parola) < 10 and ' ' not in parola:
    print('Parola prea mica')
#elif parola  # nu stiu sintaxa aici
   # print('Parola contine spatiu!')
else:
    print('Parola ok!')'''

'''Problema 2. Sa se numere de cate ori apare o litera intr-un cuvant.'''
'''
cuvant = input('Introdu cuvantul: ')
litera = input('Introdu litera: ')
numaraparitii = 0

for i in cuvant:
    if i in litera:
        numaraparitii += 1
print(f'Litera {litera} apare de {numaraparitii} ori in {cuvant}')
'''

'''Problema 3. Sa se afiseze toate toate puterile lui 3 cuprinse intre 200 si 300.'''
'''
putere = 1
while True:
    valoare = 3 ** putere
    if valoare > 300:
        break

    if 200 <= valoare <= 300:
        print(valoare)
    putere += 1

#sau

i=0
putere = 3** i
if 200 < putere < 300:
    print(f'{putere}')
'''

'''Problema 5. Rezolvati folosind doua variante: Varianta 1 -> FOR
                                                Varianta 2 -> WHILE
   Se citeste un numar n de la tastatura. Sa se scrie un program care
    face o numaratoare inversa de la numarul respectiv pana la 0.'''

#FOR
'''n = int(input(f'Introduceti numarul: '))
for i in range(0,n):
    n -= 1
    print(n)'''

#WHILE
'''n = int(input(f'Introduceti numarul: '))
while True:
    print(n)
    n -= 1
    if n == -1:
        break'''


'''Problema 6. Rezolvati folosind doua variante: Varianta 1 -> FOR
                                                Varianta 2 -> WHILE
    Se citeste un numar de la tastatura. Sa se calculeze 
        suma numerelor de la 1 pana la numarul citit. (folositi for si while)'''

#FOR
'''n = int(input(f'Introduceti numarul: '))
suma = 0

for i in range (1,n):
    suma += i
    print(suma)'''

# Cu while
'''n = int(input(f'Introduceti numarul: '))
i=1
suma = 1
while i < n:
    suma += i
    i += 1
    print(suma)'''