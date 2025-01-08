"""
    map ->
    map(func,*iterables)

    func - some fn that takes as many arguments as there are iterable objects passed to iterables
    *iterables - a variable number of iterable objects

    return an iterator that calculates the fn applied to each element of the iterables

    iterator stops  as soon as one of iterables exhaust
    so, unequal length of iterables can be used
"""

l=[1,2,3,4]
def square(x):
    return x**x

res=list(map(square,l)) # gonna apply square to each element of list 'l'
print(res)

"""
    taking in 2 lists and adding them
"""
l1=[1,2,3,4]
l2=[10,20,30]
def add(x,y):
    return x+y
print(list(map(add,l1,l2)))

# lambda to add 2 lists
res=list(map(lambda x,y:x+y, l1,l2)) # lambda is applied to 2 iterables l1 and l2

##### FILTER #####
"""
    filter -> it allows us to specify a fn that determines whether we retain 
    or throw out the elements of that iterable 
    filter(func,iterable)
    
    return an iterator that contains all the elements of the iterable for which func returns true
    if func is none - return the elements of iterable that are Truthy
"""
l=[0,1,2,3,4]
print(list(filter(None, l))) # 0 not taken

def is_even(x):
    return x % 2 == 0
print(list(filter(is_even,l)))  # evens are taken

############ ZIP #################
"""
    zip(*iterables) - operates on iterables - not a high order fn
    takes in any number of iterables and return an iterable
    combines iterables one at a time
"""
l1=[1,2,3]
l2=[10,20,30]
l3=['a','b','c']
print(zip(l1,l2,l3)) # returns iterable
print(list(zip(l1,l2,l3))) # return zipped list

####################### List Comprehensions (alternative to map) #######################
"""
    {expression} for {element} in {iterable}
"""
l1=[1,2,3]
l2=[10,20,30]

print(list(map(lambda x,y: x+y, l1,l2)))  # adding lists
print(list(zip(l1,l2))) # zipping lists
print(list(x+y for x,y in zip(l1,l2)))  # list comprehension

####################### List Comprehensions (alternative to filter) #######################
"""
    {expression} for {element} in {iterable} if {expression}
"""
l=[1,2,3,4]
print(list(filter(lambda n:n%2==0,l)))
# add if to list comprehension
print([x for x in l if x%2==0])

####################### combining map and filter #######################
print("\n")
l=range(10)
print(l)
res2=list(filter(lambda y:y<25, map(lambda x:x**2,l)))
print(res2)

res3=[x**2 for x in range(10) if x**2<25]
print(res3)











