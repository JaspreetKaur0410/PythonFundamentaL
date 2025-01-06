# lambda expression when created -  returns a fn object
# lambda [parameter-list]:expression -> anonymous/lambda fn

print(lambda:"hello")
print(lambda s:s[::-1].upper())

# these fns are not named

my_func=lambda x:x*2
print(type(my_func))
print(my_func(1))

# The body of lambda is limited to single expression - no assignments