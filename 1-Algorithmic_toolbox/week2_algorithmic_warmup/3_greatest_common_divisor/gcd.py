# Uses python3
import sys

def gcd_naive(a, b):
    if b==0:
        return a
    else:
        return gcd_naive(b,a%b)

if __name__ == "__main__":
    # input = sys.stdin.read()
    a, b = map(int, input().split())
    # p = max(a,b)
    # q=min(a,b)
    print(gcd_naive(a, b))
