def find_intersection(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    return list(set1.intersection(set2))

# Example Usage
nums1 = [1, 2, 2, 1, 3]
nums2 = [2, 2, 3, 4]
result = find_intersection(nums1, nums2)
print(f"Intersection: {result}")
