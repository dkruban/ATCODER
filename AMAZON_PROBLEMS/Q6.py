def find_starting_point(petrol, distance, N):
    start = 0
    curr_petrol = 0
    deficit = 0 
    
    for i in range(N):
        curr_petrol += petrol[i] - distance[i]
        
        if curr_petrol < 0:
          
            deficit += curr_petrol
            start = i + 1
            curr_petrol = 0
    
    if (curr_petrol + deficit) >= 0:
        return start
    return -1 
