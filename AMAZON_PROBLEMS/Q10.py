def edit_distance(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for j in range(n + 1):
        dp[0][j] = j
        
   for i in range(m + 1):
        dp[i][0] = i
        
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] # No operation needed
            else:
                # 1 + min(insert, delete, replace)
                dp[i][j] = 1 + min(
                    dp[i][j-1],      # Insert
                    dp[i-1][j],      # Delete
                    dp[i-1][j-1]     # Replace
                )
                
    return dp[m][n]
