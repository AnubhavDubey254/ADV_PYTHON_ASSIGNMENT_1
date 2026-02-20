def remove_duplicates(arr):
    seen = set()
    result = []
    for num in arr:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result

# Example Usage
nums = [1, 2, 2, 3, 4, 4, 5, 1]
unique_nums = remove_duplicates(nums)
print(f"Unique Array: {unique_nums}")
