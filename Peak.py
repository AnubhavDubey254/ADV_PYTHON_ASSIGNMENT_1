def find_peak(arr):
    n = len(arr)
    left, right = 0, n - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if mid is a peak
        if (mid == 0 or arr[mid] > arr[mid - 1]) and \
           (mid == n - 1 or arr[mid] > arr[mid + 1]):
            return mid
        
        if mid > 0 and arr[mid - 1] > arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
            
    return -1

# Example Usage
nums = [1, 2, 3, 1]
index = find_peak(nums)
print(f"Peak element found at index: {index} (Value: {nums[index]})")
