
### Loopar

for i in range(1, 10):
    print(i)

# Oftast enklast att räkna från 0 i programmering
# range(0, 10)
# range(1, 1 + 10)


for i in range(1, 4):
    for j in range(1, 4):
        print(i, "*", j, "=", i * j)

    # Lägg till det här för att visa på indenteringen        
    print("-----------")


### Modulo och villkor

# Visa rest
for i in range(1, 11):
    print(i, i % 2)

# Skriv ut jämna tal
for i in range(1, 11):
    rest = i % 2
    if rest == 0:
        print(i)

# Skriv ut om tal är udda eller jämna
for i in range(1, 11):
    rest = i % 2
    if rest == 0:
        print(i, "är jämnt")
    else:
        print(i, "är udda")


# Använd variabel istället
for i in range(1, 11):
    rest = i % 2
    if rest == 0:
        typ = "jämnt"
    else:
        typ = "udda"

    print(i, "är", typ)
