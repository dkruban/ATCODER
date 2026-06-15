def find_starting_point(petrol, distance, N):
    start = 0
    curr_petrol = 0
    deficit = 0 # Total deficit if we fail to reach end
    
    for i in range(N):
        curr_petrol += petrol[i] - distance[i]
        
        if curr_petrol < 0:
            # Cannot reach i+1 from start
            deficit += curr_petrol
            start = i + 1
            curr_petrol = 0
    
    # If we have enough to cover the deficit, start is valid
    # In this specific problem statement, a solution is guaranteed if one exists
    if (curr_petrol + deficit) >= 0:
        return start
    return -1 # No solution
