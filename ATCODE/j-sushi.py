import sys

def solve():
    # Read all inputs from standard input
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    N = int(data[0])
    sushi_counts = [int(x) for x in data[1:N+1]]
    
    # Count how many dishes have 1, 2, or 3 pieces of sushi initially
    c1 = sushi_counts.count(1)
    c2 = sushi_counts.count(2)
    c3 = sushi_counts.count(3)
    
    # dp[i][j][k] will store the expected number of moves when there are:
    # i dishes with 1 sushi
    # j dishes with 2 sushi
    # k dishes with 3 sushi
    # Initialize the 3D DP table with 0.0
    dp = [[[0.0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]
    
    # Iterate through the number of total sushi dishes from smallest to largest
    for k in range(N + 1):
        for j in range(N + 1):
            for i in range(N + 1):
                # Base case: No sushi left on any dish
                if i == 0 and j == 0 and k == 0:
                    continue
                
                # Total number of dishes that currently have at least one sushi
                total_sushi_dishes = i + j + k
                
                # If the total exceeds N, this state is impossible
                if total_sushi_dishes > N:
                    continue
                
                # Start with the expected cost of choosing a dish that has sushi
                # This accounts for the self-loop when picking an empty dish:
                # E = 1 + (N - (i+j+k))/N * E + (i/N)*E_next1 + (j/N)*E_next2 + (k/N)*E_next3
                # Rearranging terms gives the base contribution: N / (i + j + k)
                ans = N / total_sushi_dishes
                
                # Transition 1: Pick a dish with 1 sushi -> it becomes 0 sushi
                if i > 0:
                    ans += dp[i - 1][j][k] * (i / total_sushi_dishes)
                    
                # Transition 2: Pick a dish with 2 sushi -> it becomes 1 sushi
                if j > 0 and i + 1 <= N:
                    ans += dp[i + 1][j - 1][k] * (j / total_sushi_dishes)
                    
                # Transition 3: Pick a dish with 3 sushi -> it becomes 2 sushi
                if k > 0 and j + 1 <= N:
                    ans += dp[i][j + 1][k - 1] * (k / total_sushi_dishes)
                    
                dp[i][j][k] = ans

    # Output the result for our initial configuration
    print(f"{dp[c1][c2][c3]:.14f}")

if __name__ == '__main__':
    solve()
