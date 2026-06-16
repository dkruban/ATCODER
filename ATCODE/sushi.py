import sys

def main():
    # Read all input from standard input quickly
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    n = int(data[0])
    m = int(data[1])
    
    # Extract weights for shari and neta
    # data[2 : 2+n] contains A_1 to A_N
    # data[2+n : 2+n+m] contains B_1 to B_M
    shari = [int(x) for x in data[2 : 2+n]]
    neta = [int(x) for x in data[2+n : 2+n+m]]
    
    # Sort both arrays in descending order (largest to smallest)
    shari.sort(reverse=True)
    neta.sort(reverse=True)
    
    shari_ptr = 0
    neta_ptr = 0
    sushi_count = 0
    
    # Match items using two pointers
    while shari_ptr < n and neta_ptr < m:
        # Check if the current neta is small enough for the current shari
        if neta[neta_ptr] <= 2 * shari[shari_ptr]:
            # They match! Make a sushi and move both pointers
            sushi_count += 1
            shari_ptr += 1
            neta_ptr += 1
        else:
            # The neta is too heavy for this shari.
            # Since the shari array is sorted descending, this neta is also
            # too heavy for all remaining smaller shari. Skip this neta.
            neta_ptr += 1
            
    print(sushi_count)

if __name__ == '__main__':
    main()
