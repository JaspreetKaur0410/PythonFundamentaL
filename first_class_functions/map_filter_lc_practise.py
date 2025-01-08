def fact(n):
    return 1 if n<2 else n*fact(n-1)

res1=map(fact,range(5))
for x in res1:
    print(x)

# let us run loop again - doesn't print anything
for x in res1:
    print(x)

"""
    map,filter and zip doesn't return lists or tuples etc
    they return genrators which doesn't pre-calculate
    when we created map object - haven't calculated factorial yet
    but, when we request item to calculate factorial by iterating through map object, then python make calculations
    so you actually deferring the calculation till the time you actually need them
    if you want to reuse - you can't do
"""
# turn res1 to list
res1=list(map(fact,range(5)))
print("\n")
for x in res1:
    print(x)
# let us run loop again - doesn't print anything
for x in res1:
    print(x)

l1=[1,2,3]
l2=[10,20,30]
l3=[100,200,300,400]
result_3=map(lambda x,y:x+y,l1,l2,l3)
print(result_3) # doesn't give error - it doesn't make calculation right away
# for x in result_3: # gives error
#     print(x)

#### filter #######
res_4=list(filter(lambda x:x%3==0,range(25)))
print(res_4)

#### zip #######
l=[1,2,3,4]
l2=[10,20,30,40]
l3='python'
res_4=list(zip(l1,l2,l3))
print(res_4)

###### List Comprehensions ##########
"""
    List Comprehensions actually create a list and don't defer calculations
    in that sense, map is better to save time (in some cases)
"""
res_5=[fact(n) for n in range(10)]
print(res_5)

##### generator object(instead of list comprehensions - so that we can defer calculations) ########
print("\n")
res_6=(fact(n) for n in range(10))
print(res_6)
for x in res_6:
    print(x)
for x in res_6:
    print(x)

print("\n")
l1=[1,2,3,4,5,6]
l2=[10,20,30,40]

res_7=list(map(lambda x,y:x+y,l1,l2))
print(res_7)

res_8=[x+y for x,y in zip(l1,l2)]
print(res_8)

# keep elements that are even
res_9=list(
    filter(lambda x:x%2==0, map(lambda x,y:x+y,l1,l2))
)
print(res_9)

# use list comprehnsion to keep elements that are even
res_10=[x+y for x,y in zip(l1,l2) if (x+y)%2==0]
print(res_10)












