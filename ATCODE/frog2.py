import sys

def main():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    n = int(data[0])
    h = [int(x) for x in data[1:]]
    
    dp = [0] * n
    
    # Base cases
    dp[0] = 0
    if n > 1:
        dp[1] = abs(h[1] - h[0])
        
    for i in range(2, n):
        jump_one = dp[i-1] + abs(h[i] - h[i-1])
        jump_two = dp[i-2] + abs(h[i] - h[i-2])
        dp[i] = min(jump_one, jump_two)
        
    print(dp[n-1])

if __name__ == '__main__':
    main()
