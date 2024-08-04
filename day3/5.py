def find_kth_missing_positive(arr, k):
    missing = []
    current = 1
    i = 0
    while len(missing) < k:
        if i < len(arr) and arr[i] == current:
            i += 1
        else:
            missing.append(current)
        current += 1
    return missing[-1]

print(find_kth_missing_positive([2, 3, 4, 7, 11], 5))
print(find_kth_missing_positive([1, 2, 3, 4], 2))