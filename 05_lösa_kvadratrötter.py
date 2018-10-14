
# Babyloniska metoden:
# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Babylonian_method

# Talet som ska dra kvadratroten ur
S = 999

# Gissa en första kvadratrot x
x = S / 4

for i in range(1, 10):
    # Förbättra x till medelvärdet av x och S/x
    ny_x = (S / x + x) / 2
    print("iteration", i, ": x =", x, ", ny_x =", ny_x)
    x = ny_x

print("kvadratroten av", S, "är ungefär", x)
print("x ** 2 =", x ** 2)


# Förbättra till while-loop

x = S / 4

löst = False
while not löst:
    # Förbättra x till medelvärdet av x och S/x
    ny_x = (S / x + x) / 2
    diff = abs(x - ny_x)
    print("x =", x, ", ny_x =", ny_x, ", diff =", diff)
    x = ny_x

    if diff < 0.1:
        löst = True

print("kvadratroten av", S, "är ungefär", x)
print("x ** 2 =", x ** 2)
