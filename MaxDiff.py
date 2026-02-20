def find_max_difference(arr):
    if len(arr) < 2:
        return 0
    
    min_element = arr[0]
    max_diff = arr[1] - arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] - min_element > max_diff:
            max_diff = arr[i] - min_element
        
        if arr[i] < min_element:
            min_element = arr[i]
            
    return max_diff

# Example Usage
nums = [2, 3, 10, 6, 4, 8, 1]
print(f"Maximum Difference: {find_max_difference(nums)}")
