def sum_of_elements(arr):
    total = 0
    for num in arr:
        total += num
    return total

# Example Usage
nums = [10, 20, 30, 40, 50]
result = sum_of_elements(nums)
print(f"Sum: {result}")
