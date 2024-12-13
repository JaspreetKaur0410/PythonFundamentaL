# internal state changed
my_list = [1, 2, 3]
print(my_list)
print(id(my_list))
my_list.append(4)
print(id(my_list))

print("\n")

# internal state not changed
my_list_1=[1,2,3]
print(id(my_list_1))
my_list_1=my_list+[4]
print(my_list_1)
print(id(my_list_1))