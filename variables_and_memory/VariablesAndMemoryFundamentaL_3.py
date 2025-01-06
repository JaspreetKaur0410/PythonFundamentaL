# internal state changed
print("internal state changed")
my_list = [1, 2, 3]
print(id(my_list))
my_list.append(4)
print(id(my_list))

print("\n\n")

# internal state not changed
print("internal state not changed")
my_list_1=[1,2,3]
print(id(my_list_1))
my_list_1=my_list+[4]
print(id(my_list_1))

print("\n\n")
# when working with mutable objects
print("when working with mutable objects")
a=[1,2,3]
b=[1,2,3]
# b.append(4)
print(id(a))
print(id(b))
# with mutable object, the python memory manager will never create shared references