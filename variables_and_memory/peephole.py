# Memebership tests-
#     lists -> tuples
#     sets -> frozenset

def my_func():
    a=24*60
    b=(1,2)*5
    c='abc'*3
    d='ab'*11
    e='the quick brown fox'*5
    f=['a','b']*3

print(my_func.__code__.co_consts)

def my_func(e):
    if e in {1,2,3}:
        pass
print(my_func.__code__.co_consts)

# set membership is efficient than list, tuple or string
import string
import time

char_list=list(string.ascii_letters)
char_tuple=tuple(char_list)
char_set=set(string.ascii_letters)
print(char_list)
print(char_tuple)
print(char_set)
# set is not ordered - list & tuple are ordered

def membership_tes(n,container):
    for i in range(n):
        if 'z' in container:
            pass

start=time.time()
membership_tes(100000,char_list)
end=time.time()
print('list: ',end-start)

start=time.time()
membership_tes(100000,char_tuple)
end=time.time()
print('tuple: ',end-start)

start=time.time()
membership_tes(100000,char_set)
end=time.time()
print('set: ',end-start)

