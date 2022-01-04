# listák

# üres lista
lista_1 = []
# lista elemekkel
lista_2 = ['kutya', 'macska', 'egér']

# új elem hozzáadása:
lista_2.append('delfin')

lista_hossza = len(lista_2)

# lista 3. eleme:
print(lista_2[2])

# lista bejárása:
for elem in lista_2:
    print(elem)

# listába elem beszúrása pl. 2. indexre:
lista_2.insert(2, 'gyík')
print('----------------')
for elem in lista_2:
    print(elem)

print('----------------')
# lista indexeinek bejárása:
for i in range(len(lista_2)):
    print(f'{i}. {lista_2[i]}')

# lista elemeinek rendezése:
print('----------------')
lista_2.sort()
for e in lista_2:
    print(e)

# karakterláncon (string)
szoveg = 'kedvesem betegen szunnyad e hajnalon'

szoveg_hossza = len(szoveg)

# szoveg karakterenjkénti bejarasa
for k in szoveg:
    print(k, end=' ')
print('\n----------------------')
# konkatenáció
uj_szoveg = szoveg + "\nnyugodj most szerelem, szeress most nyugalom"

print(uj_szoveg)

nagybetus = uj_szoveg.upper()
print(nagybetus)
kisbetus = nagybetus.lower()
print(kisbetus)

darabok = uj_szoveg.split(' ')

for db in darabok:
    print(db)