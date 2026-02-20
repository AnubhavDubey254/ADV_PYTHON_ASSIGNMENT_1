def find_leaders(arr):
    n = len(arr)
    if n == 0:
        return []
    
    leaders = []
    max_from_right = float('-inf')
    
    for i in range(n - 1, -1, -1):
        if arr[i] > max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]
            
    return leaders[::-1]

# Example Usage
nums = [16, 17, 4, 3, 5, 2]
result = find_leaders(nums)
print(f"Leaders: {result}")
