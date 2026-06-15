def kadane(arr):
    max_so_far = float('-inf')
    current_max = 0
    for x in arr:
        current_max += x
        if max_so_far < current_max:
            max_so_far = current_max
        if current_max < 0:
            current_max = 0
    return max_so_far if max_so_far > 0 else max(arr) 

def max_sum_submatrix(M, R, C):
    max_sum = float('-inf')
    
    for left in range(C):
        temp = [0] * R
        for right in range(left, C):
            for i in range(R):
                temp[i] += M[i][right]
            
            current_max = kadane(temp)
            if current_max > max_sum:
                max_sum = current_max
                
    return max_sum
