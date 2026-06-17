import sys

def solve():
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
      
        dp = [-1] * (x + 1)
        dp[0] = 0
        
        for char in u:
           
            next_dp = list(dp)
            
            for m in range(x + 1):
                if dp[m] == -1:
                    continue
               
                if char == 'I':
                    if m < x:
                        next_dp[m+1] = max(next_dp[m+1], dp[m] + 1)
                        
               
                elif char == 'E':
                    if m > 0 and dp[m] < m * s:
                        next_dp[m] = max(next_dp[m], dp[m] + 1)
                        
              
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
