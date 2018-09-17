
### Explicit problemlösning

# Ida har 115 kr
# Pelle har 280 kr
# Hur många kronor Ida och Pelle tillsammans?

print(395)
print(115 + 280)

idas_kronor = 115
kalles_kronor = 280
kronor_totalt = idas_kronor + kalles_kronor
print(kronor_totalt)

idas_kronor = int(input("Hur många kronor har Ida?"))
kalles_kronor = int(input("Hur många kronor har Kalle?"))
kronor_totalt = idas_kronor + kalles_kronor
print("De har ", kronor_totalt, "kronor tillsammans")


person1_kronor = int(input("Hur många kronor har den första personen?"))
person2_kronor = int(input("Hur många kronor har den andra personen?"))
kronor_totalt = person1_kronor + person2_kronor
print("De har ", kronor_totalt, "kronor tillsammans")


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
print(x)
print(a * x + b, "=", c)

### Andragradsekvationer

# x^2 + px + q = 0

from math import *
print(sqrt(49))

p = 10
q = 2
x1 = -p/2 + sqrt(p ** 2 / 4 - q)
x2 = -p/2 - sqrt(p ** 2 / 4 - q)
print("Rot 1:", x1)
print("Rot 2:", x2)

p = 10
q = 2
delterm = sqrt(p ** 2 / 4 - q)
x1 = -p/2 + delterm
x2 = -p/2 - delterm
print("Rot 1:", x1)
print("Rot 2:", x2)


print(x1 ** 2 + p * x1 + q)
print(x2 ** 2 + p * x2 + q)

print(round(x1 ** 2 + p * x1 + q, 10))
print(round(x2 ** 2 + p * x2 + q, 10))

### Titta på math i dokumentationen

# Accelleration
# v0*t + a * t**2 / 2
