def calculate_navigable_airspace_optimized(heights):
    if not heights or len(heights) < 3:
        return 0

    left = 0
    right = len(heights) - 1
    
    left_max = 0
    right_max = 0
    
    total_airspace = 0

    while left < right:
        if heights[left] < heights[right]:
            if heights[left] >= left_max:
                left_max = heights[left]
            else:
                total_airspace += (left_max - heights[left])
            left += 1
        else:
            if heights[right] >= right_max:
                right_max = heights[right]
            else:
                total_airspace += (right_max - heights[right])
            right -= 1

    return total_airspace

# Test
buildings = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
result = calculate_navigable_airspace_optimized(buildings)
print(f"Total Navigable Airspace (Optimized) = {result}")

# Hidden test cases
test_cases = [
    [5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5],
    [5, 0, 0, 0, 5],
    [1000000000, 0, 1000000000]
]

for i, case in enumerate(test_cases, 1):
    print(f"Test Case {i} {case}: {calculate_navigable_airspace_optimized(case)}")
