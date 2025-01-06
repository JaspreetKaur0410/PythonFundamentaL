def square(a):
    return a*a
print(type(square))
print(id(square))
f=square
print(type(f))
print(id(square))
print(id(f))

print("\n\n")

def cube(a):
    return a**3

def select_fn(fn_id):
    if fn_id==1:
        return square
    else:
        return cube

f=select_fn(1)
print(f is square)
f=select_fn(2)
print(f is cube)

print("\n\n")
print(select_fn(2)(3))