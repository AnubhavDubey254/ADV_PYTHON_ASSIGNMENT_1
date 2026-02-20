def find_union(arr1, arr2):
    return list(set(arr1) | set(arr2))

# Example Usage
nums1 = [1, 2, 3, 4]
nums2 = [3, 4, 5, 6]
result = find_union(nums1, nums2)
print(f"Union: {result}")
