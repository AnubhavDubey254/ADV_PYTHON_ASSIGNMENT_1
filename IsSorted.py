def is_sorted(arr):
    if len(arr) <= 1:
        return True
    
    is_ascending = True
    is_descending = True
    
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            is_ascending = False
        if arr[i] < arr[i + 1]:
            is_descending = False
            
    return is_ascending or is_descending

# Example Usage
nums_asc = [10, 20, 30, 40]
nums_desc = [40, 30, 20, 10]
nums_unsorted = [10, 30, 20, 40]

print(f"Is [10, 20, 30, 40] sorted? {is_sorted(nums_asc)}")
print(f"Is [40, 30, 20, 10] sorted? {is_sorted(nums_desc)}")
print(f"Is [10, 30, 20, 40] sorted? {is_sorted(nums_unsorted)}")
