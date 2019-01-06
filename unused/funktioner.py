### Funktioner

# Refaktorera sista koden från steg 3
def udda_eller_jamnt(tal):
    rest = tal % 2
    if rest == 0:
        typ = "jämnt"
    else:
        typ = "udda"

    return typ

for i in range(1, 11):
    print(i, "är", udda_eller_jamnt(i))


# Refaktorera igen: Bygga upp flera nivåer av funktioner
def delbart_med(tal, divisor):
    rest = tal % divisor
    if rest == 0:
        return True
    else:
        return False

def udda_eller_jamnt(tal):
    if delbart_med(tal, 2):
        typ = "jämnt"
    else:
        typ = "udda"

    return typ

for i in range(1, 11):
    print(i, "är", udda_eller_jamnt(i))


### Primtal

def delbart_med(tal, divisor):
    rest = tal % divisor
    if rest == 0:
        return True
    else:
        return False

def udda_eller_jamnt(tal):
    if delbart_med(tal, 2):
        typ = "jämnt"
    else:
        typ = "udda"

    return typ

def primtal(tal):
    for i in range(2, tal):
        if delbart_med(tal, i):
            return False
    return True

for i in range(1, 11):
    print(i, "är", udda_eller_jamnt(i))
    if primtal(i):
        print(i, "är ett primtal")


# Fortsätt:
# Skriv ut alla primtal under tal X
# Räkna antal primtal under tal X

