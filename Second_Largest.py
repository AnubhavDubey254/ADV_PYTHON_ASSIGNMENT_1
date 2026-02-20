def find_second_largest(arr):
    if len(arr) < 2:
        return None
    
    first = second = float('-inf')
    
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
            
    return second if second != float('-inf') else None

# Example Usage
nums = [12, 35, 1, 10, 34, 1]
result = find_second_largest(nums)
print(f"Second Largest: {result}")
