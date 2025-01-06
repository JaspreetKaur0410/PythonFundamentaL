print(float('12.5'))
print(float(22/7))
# error - print(float('22/7'))

import fractions
a=fractions.Fraction('22/7')
print(float(a))
print(0.1)
print(format(0.1,'.25f'))
print(format(0.125,'.25f'))

print("\n")
a=0.1+0.1+0.1
b=0.3
print(a==b)
print(format(a,'.25f'))
print(format(b,'.25f'))