def find_all_subarrays(arr):
    subarrays = []
    n = len(arr)
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            subarrays.append(arr[i:j])
            
    return subarrays

# Example Usage
nums = [1, 2, 3]
result = find_all_subarrays(nums)
print(f"All Subarrays: {result}")
