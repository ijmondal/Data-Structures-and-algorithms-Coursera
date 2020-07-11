# Uses python3
def calc_fib(n, t ={0:0, 1:1}):
    if n in t:
        return t[n]
    else:
        t[n] = calc_fib(n - 1) + calc_fib(n - 2)
    return t[n]

n = int(input())
print(calc_fib(n))
