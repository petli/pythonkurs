
### Förändringsvärden

### for-loop

# Diskutera
#  * Metod att räkna ut år för år manuellt
#  * Identifiera mönstret och upprepningen

# Värdeminskning: forka repl

värde = 350000
värdeminskning = 8
antal_år = 5

for i in range(antal_år):
    värde = värde - värde * värdeminskning / 100

print("Efter", antal_år, "år är värdet", värde, "kr")

# Lägg till utskrift av värdet varje år
# Lägg till utskrift av beloppet som värdet minskar med varje år


### while-loop

# Lån:

# Diskutera:
#  * När vet vi att lånet betalats av?
#  * Kan inte använda for-loop

belopp = 100000
ränta = 3
amortering = 500

while belopp > 0:
    # Låt deltagarna skriva kroppen i while-loopen
    belopp = belopp + belopp * ränta / 100 - amortering * 12
    print(belopp)

# Lägg till uppräkning och utskrift av antal år


### Statistik

# import statistics

månader = [5, 3, 2, 12, 5, 1, 6, 10, 8]

summa = 0
for m in månader:
    print(m)
    summa = summa + m

antal_värden = len(månader)

print("Genomsnitt:", summa / antal_värden)

sorterade_månader = sorted(månader)
print(sorterade_månader)

print("Första månad:", sorterade_månader[0])
print("Sista månad:", sorterade_månader[antal_värden - 1])

mitt = int(antal_värden / 2)
print("Median:", sorterade_månader[mitt])

print("Typvärde:", statistics.mode(månader))


### Slumptal

from random import *

# Gör en massa tärningskast

svar = input("Hur många kast?")
antal_kast = int(svar)
summa = 0

for i in range(antal_kast):
    sida = randint(1, 6)
    summa = summa + sida

print("Snitt:", summa / antal_kast)

# Lägg till uträkning av hur många ettor som kastas

ettor = 0
for i in range(antal_kast):
    sida = randint(1, 6)
    summa = summa + sida
    if sida == 1:
        ettor = ettor + 1

print("Snitt:", summa / antal_kast)
print("Ettor:", ettor)

# Lägg till uträkning av hur många jämna/udda?
