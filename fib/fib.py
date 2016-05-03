fib = lambda n : n if n <=2 else fib(n-1) + fib(n-2)

def memo(func):
    cache = {}
    def warp(*args):
        if args not in cache:
            cache[args] = func(*args)
        print cache
        return cache[args]
    return warp

@memo
def fib2(n):
    if n <= 2:
        return n
    else:
        return fib2(n-1) + fib2(n-2)



print fib(1)
print fib(2)
print fib(3)

print fib2(1)
print fib2(2)
print fib2(3)
