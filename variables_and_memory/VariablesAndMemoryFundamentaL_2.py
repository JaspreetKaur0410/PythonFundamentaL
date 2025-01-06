import ctypes
import gc

def ref_count(address):
    return ctypes.c_long(address).value

def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "Object Exists"
        else:
            return "Object Not Found"

class A:
    def __init__(self):
        # call another class-b variable is set to an instance of class B passing Self(instance of A)
        # passing instance of A to B
        # B's constructor will store that reference
        self.b=B(self)
        print('A: self: {0}, b: {1}'.format(hex(id(self)),hex(id(self.b))))

class B:
    def __init__(self,a):
        self.a=a
        print('B: self: {0}, a: {1}'.format(hex(id(self)), hex(id(self.a))))




gc.disable()

my_var=A()
print(hex(id(my_var)))
print(hex(id(my_var.b)))
print(hex(id(my_var.b.a)))

print("\n")
a_id=id(my_var)
b_id=id(my_var.b)
print(hex(a_id))
print(hex(b_id))
print("\n")
print(ref_count(a_id))
print(ref_count(b_id))
print(object_by_id(a_id))
print(object_by_id(b_id))
print("\n")

my_var=None
print(ref_count(a_id))
print(ref_count(b_id))