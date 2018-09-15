

def fib(value):
    a = 0
    b = 1
    for _ in range(value):
        yield a + b
        a, b = b, a + b


# from generator import fib
# g = fib(10)
# nest(g) or list(g)