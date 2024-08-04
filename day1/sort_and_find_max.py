def sort_and_find_max(arr):
    if not arr:
        return None
    arr.sort()
    return arr[-1]
print(sort_and_find_max([]))  
print(sort_and_find_max([5]))  
print(sort_and_find_max([3, 3, 3, 3, 3]))