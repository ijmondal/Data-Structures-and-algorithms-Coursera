# Uses python3
def calc_fib(n):
    lastTwo = [0,1] #first two numbers are initialized
    counter = 3 #3rd fibonacci number 
    while counter <= n:
        nextFib = (lastTwo[0] + lastTwo[1] ) % 10
        lastTwo[0] = lastTwo[1] % 10
        lastTwo[1] = nextFib
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0]  #ternary operator

n = int(input())
print(calc_fib(n+1))
