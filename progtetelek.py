# (elemi) programozási tételek:
# - sorozatszámítás (pl.: összegzés)
# - megszámlálás
# - szélsőérték (min, max)
# --------------
# - eldöntés
# - kiválasztás
# - keresés

szamok = [26, 1, 20, 21, 5, 99, 32, 11]

# szákom összege
sum = 0
for sz in szamok:
    sum += sz
print(f'számok összege: {sum}')
# átlaga
print(f'számok átlaga: {sum/len(szamok)}')

# páros szákom száma
c = 0
for sz in szamok:
    if sz % 2 == 0:
        c += 1
print(f'páros számok száma: {c}')

# legkisebb
mini = 0
for i in range(1, len(szamok)):
    if szamok[mini] > szamok[i]:
        mini = i
print(f'leggkisebb elem: {szamok[mini]}')

# legnagyobb indexe
maxi = 0
for i in range(1, len(szamok)):
    if szamok[maxi] < szamok[i]:
        maxi = i
print(f'legnagyobb elem indexe: {maxi}')

# van-e benne 7el osztható
i = 0
while i < len(szamok) and szamok[i] % 7 != 0:
    i += 1
if i < len(szamok): print('van 7el osztható')
else: print('nincs 7el osztható')

# hányas indexű elem a 20 [CSAK HA BIZTOSAN benne van]
i = 0
while szamok[i] != 20:
    i += 1
print(f'20as szám indexe: {i}')

# van-e 33 és 40 közötti szám, 
# ha igen, melyik az első ilyen

i = 0
while i < len(szamok) and (szamok[i] < 33 or szamok[i] > 40):
    i += 1
if i < len(szamok):
    print('van 33 és 40 közötti szám')
    print(f'az első ilyen a {szamok[i]} (a {i} indexű elem)')
else: print('nincs [33; 40] közötti elem')