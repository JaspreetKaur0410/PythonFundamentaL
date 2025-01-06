print(int("123"))
# when used with String, constructor has optional parameter - base, default base is 10
print(int("1010",2))
print(int("A12F",16))

print("\n\n")
import fractions
a=fractions.Fraction(22,7)
print(a)
print(float(a))

print("\n")
from fractions import Fraction
b=0.3
print(b)
print(Fraction(b))
print(format(b,'0.5f'))
print(format(b,'0.25f'))

print("\n")
x=Fraction(0.3)
print(x.limit_denominator(10))
