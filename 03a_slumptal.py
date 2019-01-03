from random import *

# Gör en massa tärningskast

svar = input("Hur många kast?")
antal_kast = int(svar)
summa = 0

for i in range(antal_kast):
    sida = randint(1, 6)
    summa = summa + sida

print("Snitt:", summa / antal_kast)


# Hur många sexor?

svar = input("Hur många kast?")
antal_kast = int(svar)
summa = 0
sexor = 0

for i in range(antal_kast):
    sida = randint(1, 6)
    summa = summa + sida
    if sida == 6:
        sexor = sexor + 1

print("Snitt:", summa / antal_kast)
print("Sexor:", sexor)



