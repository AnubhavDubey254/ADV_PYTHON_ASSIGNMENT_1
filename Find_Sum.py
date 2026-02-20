def find_pair(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Example Usage
nums = [2, 7, 11, 15]
target_val = 9
result = find_pair(nums, target_val)
print(f"Indices of pair: {result}")
