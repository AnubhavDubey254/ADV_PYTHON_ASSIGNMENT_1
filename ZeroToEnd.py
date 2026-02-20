def move_zeroes(arr):
    position = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[position], arr[i] = arr[i], arr[position]
            position += 1
    return arr

# Example Usage
nums = [0, 1, 0, 3, 12]
result = move_zeroes(nums)
print(f"Moved Zeroes: {result}")
