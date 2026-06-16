import sys

def main():
    # Read all inputs from standard input efficiently
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    n = int(data[0])
    
    # dp array stores the max happiness ending in activity A, B, or C
    # Initialize with the first day's values
    dp = [int(data[1]), int(data[2]), int(data[3])]
    
    idx = 4
    # Process the remaining days
    for _ in range(1, n):
        a = int(data[idx])
        b = int(data[idx+1])
        c = int(data[idx+2])
        idx += 3
        
        # Calculate the max happiness for today based on yesterday's choices
        next_a = a + max(dp[1], dp[2])
        next_b = b + max(dp[0], dp[2])
        next_c = c + max(dp[0], dp[1])
        
        # Update the dp array for the next day
        dp = [next_a, next_b, next_c]
        
    # The answer is the maximum value on the final day
    print(max(dp))

if __name__ == '__main__':
    main()
