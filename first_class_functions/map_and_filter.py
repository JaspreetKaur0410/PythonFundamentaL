"""
    map ->
    map(func,*iterables)
    *iterables - a variable number of iterable objects
    func - some fn that takes as many arguments as there are iterable objects passed to iterables
    return an iterator that calculates the fn applied to each element of the iterables
    iterator stops  as soon as one of iterables exhaust
    so, unequal length of iterables can be used
"""

l=[1,2,3,4]
def square(x):
    return x**x

res=list(map(square,l))
print(res)





