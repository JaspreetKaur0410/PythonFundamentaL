print(callable("abc".upper))    # true - testing if upper is callable
print(callable("abc".upper()))  # false - testing what upper is returning

# we can make instances of classes callable with - __call__
class MyClass:
    def __init__(self, x=0):
        print("something")
        self.counter=x
    def __call__(self, x=1):
        print("updating counter")
        self.counter+=x

b=MyClass()
print(b.counter)
MyClass.__call__(b,10)
print(b.counter)
print(callable(b))
b()
print(b.counter)
b()
print(b.counter)
b()
print(b.counter)



