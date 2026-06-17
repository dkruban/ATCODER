import sys

def solve():
    # Fast I/O
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    t = int(data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        n = int(data[idx])
        x = int(data[idx+1])
        s = int(data[idx+2])
        u = data[idx+3]
        idx += 4
        
        # dp[M] stores the max people seated with exactly M non-empty tables
        dp = [-1] * (x + 1)
        dp[0] = 0
        
        for char in u:
            # Create a copy for the next state transitions
            next_dp = list(dp)
            
            for m in range(x + 1):
                if dp[m] == -1:
                    continue
                
                # Option 1: Introvert ('I')
                if char == 'I':
                    if m < x:
                        next_dp[m+1] = max(next_dp[m+1], dp[m] + 1)
                        
                # Option 2: Extrovert ('E')
                elif char == 'E':
                    if m > 0 and dp[m] < m * s:
                        next_dp[m] = max(next_dp[m], dp[m] + 1)
                        
                # Option 3: Ambivert ('A')
                elif char == 'A':
                    if m < x:
                        next_dp[m+1] = max(next_dp[m+1], dp[m] + 1)
                    if m > 0 and dp[m] < m * s:
                        next_dp[m] = max(next_dp[m], dp[m] + 1)
            
            dp = next_dp
            
        out.append(str(max(dp)))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
