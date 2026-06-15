def search_rotated(A, N, key):
    low, high = 0, N - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if A[mid] == key:
            return mid
        
        if A[low] <= A[mid]:
            if A[low] <= key < A[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if A[mid] < key <= A[high]:
                low = mid + 1
            else:
                high = mid - 1
                
    return -1
