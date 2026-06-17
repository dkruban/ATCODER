import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    t = int(data[0])
    out = []
    
    for i in range(1, t + 1):
        n = int(data[i])
        
        half = (n + 1) // 2
        
        left_half = list(range(n + 1, n + 1 + half))
        right_half = list(range(n + 1 + half, 2 * n + 1))
        
        ans = []
        l_idx, r_idx = 0, 0
        
        for j in range(n):
            if j % 2 == 0:
                ans.append(str(left_half[l_idx]))
                l_idx += 1
            else:
                ans.append(str(right_half[r_idx]))
                r_idx += 1
                
        out.append(" ".join(ans))
        
    print("\n".join(out))

if __name__ == '__main__':
    solve()
