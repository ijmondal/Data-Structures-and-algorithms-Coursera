# Uses python3
import sys

def optimal_summands(n):
    summands = [1]
    #write your code here
    i=1
    while True:
        if n - sum(summands) > summands[i-1]:
            summands.append(i+1)
        elif n - sum(summands) <= summands[i-1]:
            summands[i-1] = summands[i-1] + n - sum(summands)
            return summands
        i +=1

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
