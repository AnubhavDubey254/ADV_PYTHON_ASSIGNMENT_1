def count_frequencies(arr):
    freq_map = {}
    for num in arr:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1
    return freq_map

# Example Usage
nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
frequencies = count_frequencies(nums)
print(f"Frequencies: {frequencies}")
