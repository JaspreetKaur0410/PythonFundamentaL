# packed values referes to values that are bundled in some way

# unpacking happens in python coz RHS is first evaluated and completed
# then assignments are made to LHS
a=10
b=20
a,b=b,a
print(a)
print(b)

# we don't always have to unpack every item in an iterable
# maybe we need to unpack first value, and then unpack remaining values in another variable
# we can use * operator for this - applies to any iterable(not just sequence types
l=[1,2,3,4,5,6]
a, *b=l
print(a)
print(b)

# * operator in RHS
l1=[1,2,3]
l2=[4,5,6]
l=[*l1,*l2]
print(l)

d1={'p':1,'q':2}
d2={'t':3,'h':4}
d3={'h':5,'o':6,'p':7}
# unpack the dictionary inside the list
# * operator in RHS
l=[*d1,*d2,*d3]
print(l)
# unpack into sets
s={*d1,*d2,*d3}
print(s)