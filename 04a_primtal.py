
# Hur vet man om ett tal är ett primtal?

tal = 9
for i in range(2, tal):
    kvot = tal // i
    rest = tal - kvot * i

    if rest == 0:
        print(tal, "är inte ett primtal")

# Ändra tal till 15:
# Varför skriver den ut två gånger?
# Lägg in spårutskrift på i för att undersöka

tal = 15
for i in range(2, tal):
    print("testar med", i)
    if tal % i == 0:
        print(tal, "är inte ett primtal")
        break

# Ändra till primtal 7
# Hur kan vi skriva ut om det är ett primtal?       

tal = 7
primtal = True
for i in range(2, tal):
    print("testar med", i)
    if tal % i == 0:
        primtal = False
        break

if primtal:
    print(tal, "är ett primtal")
else:
    print(tal, "är inte ett primtal")
