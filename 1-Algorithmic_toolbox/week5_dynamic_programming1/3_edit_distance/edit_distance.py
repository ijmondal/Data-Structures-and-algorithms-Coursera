# Uses python3
def edit_distance(s, t):
    #write your code here
    t_len = len(t)
    s_len = len(s)
    dp = [[0 for x in range(t_len + 1)] for x in range(s_len + 1)]
    for i in range(s_len+1):
        for j in range(t_len+1):
            if i==0:
                dp[i][j] = j
            elif j==0:
                dp[i][j] = i
            elif s[i-1] == t[j-1]: 
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert 
                                   dp[i-1][j],        # Remove 
                                   dp[i-1][j-1])      # Replace
            
    return dp[s_len][t_len] 

if __name__ == "__main__":
    print(edit_distance(input(), input()))
