def merge_sorted_arrays(arr1, arr2):
    n1, n2 = len(arr1), len(arr2)
    merged = []
    i = j = 0
    
    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
            
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    
    return merged

# Example Usage
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
result = merge_sorted_arrays(list1, list2)
print(f"Merged Array: {result}")
