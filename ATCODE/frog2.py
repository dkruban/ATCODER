import sys

def main():
    # Read all input from standard input
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    n = int(data[0])
    h = [int(x) for x in data[1:]]
    
    # dp[i] will store the minimum cost to reach stone i
    dp = [0] * n
    
    # Base cases
    dp[0] = 0
    if n > 1:
        dp[1] = abs(h[1] - h[0])
        
    # Fill the DP table for the remaining stones
    for i in range(2, n):
        # Option 1: Jump from the previous stone (i-1)
        jump_one = dp[i-1] + abs(h[i] - h[i-1])
        # Option 2: Jump from two stones back (i-2)
        jump_two = dp[i-2] + abs(h[i] - h[i-2])
        
        # Take the minimum of both choices
        dp[i] = min(jump_one, jump_two)
        
    # The answer is the cost to reach the last stone (N-1 in 0-indexed)
    print(dp[n-1])

if __name__ == '__main__':
    main()
