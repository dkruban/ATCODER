import sys

def solve():
    # Read all input from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    N = int(input_data[0])
    p = [float(x) for x in input_data[1:]]
    
    # dp[j] stores the probability of getting exactly j heads
    dp = [0.0] * (N + 1)
    dp[0] = 1.0  # Base case: 0 coins tossed, 0 heads has a probability of 1
    
    # Iterate through each coin
    for i in range(N):
        p_i = p[i]
        # Update backwards to use the values from the previous coin state
        for j in range(i + 1, -1, -1):
            # Probability of getting j heads with i+1 coins
            tails_prob = dp[j] * (1.0 - p_i) if j <= i else 0.0
            heads_prob = dp[j - 1] * p_i if j > 0 else 0.0
            dp[j] = tails_prob + heads_prob
            
    # Sum up the probabilities where the number of heads is greater than tails
    # More heads than tails means heads > N // 2
    ans = sum(dp[(N // 2) + 1:])
    
    # Print the result with high precision
    print(f"{ans:.10f}")

if __name__ == '__main__':
    solve()
