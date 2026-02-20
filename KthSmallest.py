def kth_smallest(arr, k):
    if k < 1 or k > len(arr):
        return None
    
    def partition(left, right):
        pivot = arr[right]
        i = left
        for j in range(left, right):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[right] = arr[right], arr[i]
        return i

    def select(left, right, k_idx):
        if left == right:
            return arr[left]
        
        pivot_index = partition(left, right)
        
        if k_idx == pivot_index:
            return arr[k_idx]
        elif k_idx < pivot_index:
            return select(left, pivot_index - 1, k_idx)
        else:
            return select(pivot_index + 1, right, k_idx)

    return select(0, len(arr) - 1, k - 1)

# Example Usage
nums = [7, 10, 4, 3, 20, 15]
k_val = 3
result = kth_smallest(nums, k_val)
print(f"{k_val}rd Smallest Element: {result}")
