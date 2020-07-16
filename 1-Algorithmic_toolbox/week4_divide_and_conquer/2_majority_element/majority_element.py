# Uses python3
import sys

# def get_majority_element(a, left, right):
#     if left == right:
#         return -1
#     if left + 1 == right:
#         return a[left]
#     #write your code here
#     return -1

def get_majority_element(a,n):
    d={}
    for i in range(n):
        if a[i] not in d:
            d[a[i]]=1
        elif a[i] in d:
            d[a[i]] += 1
    # print(d)
    keyMax = max(d, key=d.get)
    if d[keyMax] > n // 2:
        return 1
    else:
        return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, n) != -1:
        print(1)
    else:
        print(0)
