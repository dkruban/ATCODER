import sys

def solve():
  
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    ratings = [int(x) for x in input_data[1:]]
    
    
    fixed_colors = set()
   
    free_choice_count = 0
    
    for r in ratings:
        bucket = r // 400
        if bucket < 8:
            fixed_colors.add(bucket)
        else:
            free_choice_count += 1
            
    unique_fixed = len(fixed_colors)
    

    min_colors = max(1, unique_fixed) if unique_fixed == 0 else unique_fixed
    
.
    max_colors = unique_fixed + free_choice_count
    
    print(f"{min_colors} {max_colors}")

if __name__ == '__main__':
    solve()
