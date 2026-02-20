def remove_element(arr, val):
    index = 0
    for i in range(len(arr)):
        if arr[i] != val:
            arr[index] = arr[i]
            index += 1
    return arr[:index]

# Example Usage
nums = [3, 2, 2, 3, 4, 3]
value_to_remove = 3
result = remove_element(nums, value_to_remove)
print(f"Array after removal: {result}")
