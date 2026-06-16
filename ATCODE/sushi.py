import sys

def main():
   
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    n = int(data[0])
    m = int(data[1])
    
    shari = [int(x) for x in data[2 : 2+n]]
    neta = [int(x) for x in data[2+n : 2+n+m]]
    
    shari.sort(reverse=True)
    neta.sort(reverse=True)
    
    shari_ptr = 0
    neta_ptr = 0
    sushi_count = 0
    
    while shari_ptr < n and neta_ptr < m:
        if neta[neta_ptr] <= 2 * shari[shari_ptr]:
            sushi_count += 1
            shari_ptr += 1
            neta_ptr += 1
        else:
            neta_ptr += 1
            
    print(sushi_count)

if __name__ == '__main__':
    main()
