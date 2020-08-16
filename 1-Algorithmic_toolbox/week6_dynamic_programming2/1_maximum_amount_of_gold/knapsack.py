# Uses python3
import sys

def optimal_weight(W, wt):
    # write your code here
    result = 0
    dp = [[0 for x in range(W + 1)] for x in range(len(wt) + 1)] 
    for i in range(len(wt)+1):
        for w in range(W+1):
            if i == 0 or w == 0: 
                dp[i][w] = 0
            elif wt[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], wt[i-1]+dp[i-1][w-wt[i-1]])
            else:
                dp[i][w] = dp[i-1][w]
        
    
    # print(dp)       
    return dp[len(wt)][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W,w))
