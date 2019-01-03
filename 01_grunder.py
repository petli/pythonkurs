
### print

print("Hello world!")

# Enkla syntaxfel
#print(Hello world!)
#print("Hello world!)
#print("Hello world!"

# Blanktecken kan (oftast!) läggas in varsom
print  ( "Hello world!"    )


### Heltal

# Måste använda print för att se något
47 + 55
print(47 + 55)

# Strängar vs tal:
print("47" + "55")
print("47" + 55)
print(47 + "55")

### Fler räknesätt

print(47 - 55)
print(47 * 55)
print(47 * 55 - 12)
print(47 * (55 - 12))

# Division 
print(48 / 6)
print(48 / 10)
print(48 / 100)

# Ojämna decimaltal
print(48 / 9)
print(1 - 0.7)

# Decimalpunkt!
print(3,14159)
print(2 * 3,14159)

### Mer komplicerade utskrifter

print("Summan av", 47, "och", 55, "är", 47 + 55)


### Variabler

tal = 7
print(tal)
print(tal + 1)
print(tal + tal)
tal = 3
print(tal)

# Spara resultat
a = 7
b = 3
summa = a + b
print(summa)

# Bara variabelnamn till vänster
# a + b = summa

# Variabelnamn
namn1 = "Ida"
# 2namn = "Pelle"
# namn 3 = "Maja"

cirkelns_diameter = 5
pi = 3.14
cirkelns_omkrets = cirkelns_diameter * pi
print(cirkelns_omkrets)

a = 10
A = 20
print(a)
print(A)


### Input

namn = input()
print(namn)

namn = input("Hej, vad heter du?")
print("Hej", namn, "!")


diameter = input("Vad är cirkelns diameter")
print("Omkretsen är", diameter * 3.14)

svar = input("Vad är cirkelns diameter")
diameter = int(svar)
diameter = float(svar)

diameter = float(input("Vad är cirkelns diameter"))


### Förstagradsekvationer

# 10x + 5 = 50
# 10x = 50 - 5
# 10x = 45
# x = 45 / 10
# x = 4.5

# ax + b = c
# ax = c - b
# x = (c - b) / a

a = 10
b = 5
c = 50
x = (c - b) / a
print("x = ", x)
print("Kontroll:", a * x + b, "=", c)

# Ändra till att läsa in a b och c

svar = input("Vad är a?")
a = float(svar)

svar = input("Vad är b?")
b = float(svar)

svar = input("Vad är c?")
c = float(svar)

# Övning: skriv ett nytt program som frågar efter längden på två
# kateter i en rätvinklig triangel och räknar ut hypotenusan
