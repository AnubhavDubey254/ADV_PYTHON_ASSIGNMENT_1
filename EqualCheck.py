def are_arrays_equal(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    
    counts = {}
    for num in arr1:
        counts[num] = counts.get(num, 0) + 1
        
    for num in arr2:
        if num not in counts or counts[num] == 0:
            return False
        counts[num] -= 1
        
    return True

# Example Usage
list1 = [1, 2, 3, 2]
list2 = [2, 1, 2, 3]
list3 = [1, 2, 3, 4]

print(f"Are list1 and list2 equal? {are_arrays_equal(list1, list2)}")
print(f"Are list1 and list3 equal? {are_arrays_equal(list1, list3)}")
