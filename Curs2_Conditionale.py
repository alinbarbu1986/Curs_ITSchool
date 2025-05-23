''' O conditie este o expresie care poate fi adevarata(True) sau falsa(False).
Pe baza ei, putem decide daca anumite blocuri de cod se vor executa sau nu.'''

'''
if conditie:
    codul se executa daca conditia este adevarata(True)
elif:
    codul se executa daca prima conditie nu a fost True, dar aceasta este
else:
    codul se executa daca niciuna din conditiile de mai sus nu a fost adevarata
'''

# exemplu

'''varsta = 18 

if varsta >= 18:
    print("Ai voie sa votezi")
    if varsta == 18:
        print("major")
else:
    print("Esti inca prea tanar ca sa mergi la vot")'''

'''
Operatori de comparatie

== -> Egal cu Ex: a == b
!= -> Diferit de Ex: a != b
> -> Mai mare decat Ex: a > b
< -> Mai mic decat Ex: a < b
>= -> Mai mare sau egal ex: a >= b
<= -> Mai mic sau egal ex: a <= b

'''
# exemple operatori de comparatie
# ==
#numar = 10

'''if numar == 11:
    print("primul if")
else:
    print("al doilea if")'''

# !=

'''if numar != 1:
    print("Numarul este diferit de 1")
else:
    print("Numarul este 1")'''

# > sau <

'''temperatura = 30

if temperatura < 25:
    print("E cald afara")
else:
    print("E totusi frigut")'''

'''
Operatori logici

and -> ambele conditii trebuie sa fie True
or -> cel putin o conditie trebuie sa fie True
not -> inverseaza valoarea

'''
#Exemple operatori logici
# and

'''varsta = 20
nationalitate = 'roman'

if varsta >= 18 and nationalitate == 'roman':
    print("Poti vota in Romania")'''

# or

'''zi = 'sambata'

if zi == 'sambata' or zi == 'duminica':
    print("Este weekend")
else:
    print("Alta zi")'''

# not

'''vremea = False

if not vremea:
    print("Putem iesi in oras")
else:
    print("Ploua, stam in casa")'''

'''
Valori considerate falsy in Python:
 - None
 - False
 -0 (orice numar zero)
 - '' (sir gol)
 - [] (lista goala)
 - {} (dictionar gol)
 - set() (set gol)
 -() (tuplu gol)
'''
# exemplu 1
'''x = 0

if not x:
    print("Este zero")

#exemplu 2
x = ''

if not x:
    print("Este string gol")

#exemplu 3
x = [1, 2, 3]

if not x:
    print("Lista e goala")
else:
    print("Lista contine elemente")'''

'''x = 3

if x % 2 == 0: print("Par")

x = 7
rezultat = "par" if x % 2 == 0 else "Impar"
print(rezultat)'''

'''litera = 'a'

if litera in 'aeiou':
    print("Este vocala")'''

'''x = 7

if 5 < x < 10:
    print(f"{x} este intre 5 si 10")

nume = 'Alex'

if nume:
    print("Ai introdus un nume")'''

#nested if

'''varsta = int(input("Introdu varsta ta:"))

if varsta >= 18:
    print("Esti adult")

    if varsta >= 65:
        print("Esti pensionar")
    else:
        print("Esti in campul muncii")
else:
    print("Esti minor")'''

'''numar = int(input("Numarul ales: "))

if numar % 2 == 0:
    print(f"Numarul {numar} este par")
else:
    print(f"Numarul {numar} este impar")'''

'''numar = int(input("Numarul ales: "))

if numar > 0 and numar % 2 == 0:
    print("Pozitiv si par")
elif numar < 0 and numar % 2 != 0:
    print("Negativ si impar")
elif numar < 0 and numar % 2 == 0:
    print("negativ si par")
elif numar > 0 and numar % 2 != 0:
    print("Pozitiv si impar")
else:
    print("Zero")'''

'''
nr1 = int(input('Primul nr este: '))
nr2 = int(input('Al doilea nr este: '))

if nr1 > nr2:
    print(f'Numarul {nr1} este mai mare')
elif nr1 < nr2:
    print(f'Numarul {nr2} este mai mare')
else:
    print("Numerele sunt egale")


an = int(input('Anul ales este:'))
if (an % 4 == 0 and an % 100 != 0) or (an % 400 == 0):
    print('An bisect')
else:
    print('An normal') '''