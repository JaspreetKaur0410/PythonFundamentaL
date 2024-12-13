import sys
import ctypes

my_var=10
print(hex(id(my_var)))
my_var2=10
print(hex(id(my_var2)))

a=[1,2,3]
print(sys.getrefcount(a))
address=id(a)
print(ctypes.c_long.from_address(address).value)

a_id=id(a)
a=None
print(hex(id(a_id)))
print(hex(id(a_id)))
address=id(a_id)
print(ctypes.c_long.from_address(address).value)