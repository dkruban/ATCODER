import sys

def solve():
    # Read all inputs from standard input efficiently
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    N = int(input_data[0])
    K = int(input_data[1])
    h = [int(x) for x in input_data[2:N+2]]
    
    # dp[i] will store the minimum cost to reach Stone i
    # Initialize all values with infinity, except the starting stone
    dp = [float('inf')] * N
    dp[0] = 0  # Cost to stay on the first stone is 0

    # Iterate through each stone starting from the second one
    for i in range(1, N):
        # The frog can jump to stone i from any stone j that is up to K steps behind
        # We must make sure we don't look past the first stone (j >= 0)
        start_j = max(0, i - K)
        
        # Track the minimum cost to reach stone i from all valid previous stones
        min_cost = float('inf')
        for j in range(start_j, i):
            cost = dp[j] + abs(h[i] - h[j])
            if cost < min_cost:
                min_cost = cost
                
        dp[i] = min_cost

    # The answer is the minimum cost to reach the last stone (index N-1)
    print(dp[N - 1])

if __name__ == '__main__':
    solve()
