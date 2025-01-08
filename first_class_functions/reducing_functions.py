"""
    reducing_functions - that recombine an iterable recursively, ending up with a single return value
    also called accumulators/aggregators/folding-fns
"""
# maximum value in a sequence
l=[5,8,6,10,9]
max_value=lambda a,b:a if a>b else b

def _reduce(sequence):
    res=sequence[0]
    for e in sequence[1:]:
        res=max_value(res,e)
    return res
print(_reduce(l))

print("\n")

######### reduce ###########
"""
    works on any iterable
    
"""
from functools import reduce
l=[5,8,6,10,9]
r1=reduce(lambda a,b:a if a>b else b,l)
r2=reduce(lambda a,b:a if a<b else b,l)
print(r1,r2)