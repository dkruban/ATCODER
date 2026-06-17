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
        k = int(data[idx+1])
        s = data[idx+2]
        idx += 3
        
        # Track the count of '1's for each remainder modulo k
        ones_count = [0] * k
        for i in range(n):
            if s[i] == '1':
                ones_count[i % k] += 1
        
        # Check if every track has an even number of '1's
        possible = True
        for count in ones_count:
            if count % 2 != 0:
                possible = False
                break
                
        if possible:
            out.append("YES")
        else:
            out.append("NO")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
