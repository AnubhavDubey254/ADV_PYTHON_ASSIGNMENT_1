def rotate_left(arr, k):
    n = len(arr)
    if n == 0:
        return arr
    k = k % n
    
    def reverse(sub_arr, start, end):
        while start < end:
            sub_arr[start], sub_arr[end] = sub_arr[end], sub_arr[start]
            start += 1
            end -= 1
            
    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)
    reverse(arr, 0, n - 1)
    return arr

# Example Usage
nums = [1, 2, 3, 4, 5]
k_val = 2
result = rotate_left(nums, k_val)
print(f"Left Rotated Array: {result}")
