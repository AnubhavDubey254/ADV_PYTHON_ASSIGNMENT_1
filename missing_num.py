def find_missing_number(arr, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

# Example Usage
nums = [1, 2, 4, 5, 6]
n_val = 6
missing = find_missing_number(nums, n_val)
print(f"Missing Number: {missing}")
