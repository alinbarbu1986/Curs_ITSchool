'''Problema 1. Operatii aritmetice
Scrie un program care:
    - Cere doua numere si calculeaza:
        - Suma
        - Diferenta
        - Produsul
        - Impartirea
        - Imaprtirea intreaga
        - Restul impartirii (modulo)
        - Puterea
    - La final, afiseaza fiecare rezultat


#Incepe de aici problema 1
numar1 = int(input(f'Numarul 1 este: '))
numar2 = int(input(f'Numarul 2 este: '))

print(f"Suma este: {numar1 + numar2}")
print(f"Diferenta este: {numar1 - numar2}")
print(f"Produsul este: {numar1 * numar2}")
print(f"Impartirea este: {numar1 / numar2}")
print(f"Impartirea intreaga este: {numar1 // numar2}")
print(f"Restul impartirii este: {numar1 % numar2}")
print(f"Puterea este: {numar1 ** numar2}")
#Sfarsit problema 1
'''

'''Problema 2. Tipuri de date
Declara cate o variabila pentru fiecare tip de date studiat si afiseaza tipul acesteia


#Incepe de aici problema 2
nume = 'Alin'
varsta = 20
media = 9.90
absolvit = True
numar_complex = 2 + 3j
print(f"Nume: {nume} este un string si are varsta de {varsta} care este un int si a obtinut media {media} care este un float si este {absolvit} (boolean) avand {numar_complex} care este numar complex")
#Sfarsit problema 2
'''

''' Problema 3. Transforma din minute in ore si minute
    - Primeste de la tastatura un numar de minute(ex. 135)
    - Afiseaza cate ore si minute reprezinta acel numar


#Incepe de aici problema 3
numar = int(input(f'Introdu numarul de minute: '))

ore = numar // 60
rest = numar % 60
minute = rest // 1
print(f'Ore: {ore}')
print(f'Minute: {minute}')
#Sfarsit problema 3
'''

''' Problema 4. Bonul de cumparaturi
O persoana cumpara 3 produse. Vrem sa afisam:
    - Totalul fara TVA
    - TVA(ex. 19%)
    - Totalul cu TVA


#Incepe de aici problema 4
produs1 = float(input(f'Pret produs 1 este: '))
produs2 = float(input(f'Pret produs 2 este: '))
produs3 = float(input(f'Pret produs 3 este: '))

total_fara_tva = produs1+produs2+produs3
tva = 19*(produs1+produs2+produs3)/100
total_cu_tva = total_fara_tva + (19*(produs1+produs2+produs3)/100)

print(f'Totalul fara TVA este: {total_fara_tva}')
print(f'TVA este: {tva}')
print(f'Totalul cu TVA este: {total_cu_tva}')
#Sfarsit problema 4
'''

'''Problema 5. Bugetul pentru un concediu
Cerinta: Un grup de prieteni planuieste o vacanta. Trebuie sa calculezi: 
    - Contributia totala
    - Costul cheltuielilor (transport, cazare, mancare pe zile)
    - Ce suma ramane pentru distractii

Date de intrare: 
    - Numarul de prieteni
    - Suma de bani per persoana
    - Costul transportului
    - Costul pe zi pentru cazare
    - Costul pe zi pentru mancare
    - Numarul de zile


#Incepe de aici problema 5
numar_prieteni = int(input(f'Numarul de prieteni este: '))
suma_per_persoana = float(input(f'Suma de bani per persoana este: '))
cost_transport = float(input(f'Costul transportului este: '))
cost_cazare = float(input(f'Costul pe zi pentru cazare este: '))
cost_mancare = float(input(f'Costul pe zi pentru mancare este: '))
nr_zile = int(input(f'Numarul de zile este: '))

contributia_totala = numar_prieteni * suma_per_persoana
cost_cheltuieli_pe_zile = (cost_transport/nr_zile+cost_cazare+cost_mancare)
distractii = contributia_totala-cost_cheltuieli_pe_zile*nr_zile

print(f'Contributia totala este: {contributia_totala}')
print(f'Costul cheltuielilor (transport, cazare, mancare pe zile) este: {cost_cheltuieli_pe_zile}')
print(f'Suma ramasa pentru distractii este: {distractii}')
#Sfarsit problema 5
'''