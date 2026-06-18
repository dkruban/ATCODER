import sys

def solve():
    # Read all tokens from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    ratings = [int(x) for x in input_data[1:]]
    
    # Track unique categories for fixed colors (buckets 0 to 7)
    fixed_colors = set()
    # Track the count of users who can choose any color (bucket 8+)
    free_choice_count = 0
    
    for r in ratings:
        bucket = r // 400
        if bucket < 8:
            fixed_colors.add(bucket)
        else:
            free_choice_count += 1
            
    unique_fixed = len(fixed_colors)
    
    # Calculate Minimum Colors
    # If there are existing fixed colors, free users can match them.
    # If there are no fixed colors, everyone is free, but they must pick at least 1 color.
    min_colors = max(1, unique_fixed) if unique_fixed == 0 else unique_fixed
    
    # Calculate Maximum Colors
    # Every free user chooses a completely unique new color.
    max_colors = unique_fixed + free_choice_count
    
    print(f"{min_colors} {max_colors}")

if __name__ == '__main__':
    solve()
