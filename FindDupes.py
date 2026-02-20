def find_duplicates(arr):
    seen = set()
    duplicates = set()
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

# Example Usage
nums = [1, 2, 3, 2, 4, 5, 1, 6]
result = find_duplicates(nums)
print(f"Duplicates: {result}")
