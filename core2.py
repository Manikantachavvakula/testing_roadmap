# --------- Functions ----------
def normal_add(a, b):
    return a + b

print(normal_add(5, 3))

# --------- *args, **kwargs ----------
def show_args_kwargs(a, *args, **kwargs):
    print("a:", a)
    print("args:", args)
    print("kwargs:", kwargs)

show_args_kwargs(1, 2, 3, x=10, y=20)

# --------- Recursion ----------

def recursionn(n):
    if n == 0 :
        return 
    else : 
        recursionn(n-1)
        print(n)

recursionn(5)

# --------- Lambda, map, filter, reduce ----------
nums = [1, 2, 3, 4, 5]

tripled = list(map(lambda x: x * 3, nums))
print(tripled)

evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

from functools import reduce
total = reduce(lambda x, y: x + y, nums)
print(total)

# --------- Decorators ----------

def extra(func):
    def wrapper(a,b):
        if a>b :
            return func(a,b)
        else : 
            return "a is smaller than b"
    return wrapper 

@extra
def add(a,b):
    return a+b

print(add(5,4))
print(add(1,10))