import random 

tantargy = ['Matek', 'Fizika', 'Történelem', 'Irodalom', 'Kémia']
szam = random.randint(1,5)

print(szam, random.choice(tantargy))

if szam>3:
    print("Na ez a nem mindegy")
elif szam<3:
    print("Tanulni kéne basszameg")
else:
    print("Elmegy")
