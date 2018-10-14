
# Funktion med en parameter
def f(x):
    return 3 * x - 5

for i in range(1, 11):
    print("f(", i, ") =", f(i))

# Funktion med två parametrar
def g(x, y):
    return x ** 2 / y

for i in range(1, 4):
    for j in range(1, 4):
        print("g(", i, ",", j, ") =", g(i, j))


# Lösa förstagradsfunktion a * x + b = 0
# Vad är a och b?

b = f(0)
a = (f(10) - f(0)) / 10

print("a =", a)
print("b =", b)


