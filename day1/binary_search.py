def binary_search(arr, key):
    arr.sort()
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return f"Element {key} is found at position {mid}"
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return f"Element {key} is not found"
arr1 = [3, 4, 6, -9, 10, 8, 9, 30]
key1 = 10
key2 = 100
print(binary_search(arr1, key1)) 
print(binary_search(arr1, key2)) 