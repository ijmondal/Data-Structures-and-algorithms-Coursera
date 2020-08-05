# Uses python3
import sys

def get_change(m):
    #write your code here
    coins = [1,3,4]
    ways = [0] + ([m+1]*m)
    
    for i in range(1, m+1):
        for j in coins:
            if i >=j:
                ways[i] = min(ways[i], 1+ways[i-j])
    
    return ways[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
