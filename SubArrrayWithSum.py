def find_subarray_with_sum(arr, target):
    current_sum = 0
    start = 0
    
    for end in range(len(arr)):
        current_sum += arr[end]
        
        while current_sum > target and start < end:
            current_sum -= arr[start]
            start += 1
            
        if current_sum == target:
            return [start, end]
            
    return -1

# Example Usage
nums = [1, 4, 20, 3, 10, 5]
target_val = 33
result = find_subarray_with_sum(nums, target_val)
print(f"Subarray indices: {result}")
