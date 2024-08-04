def count_pairs(nums, k):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j] and (i * j) % k == 0:
                count += 1
    return count
nums1 = [3, 1, 2, 2, 2, 1, 3]
k1 = 2
nums2 = [1, 2, 3, 4]
k2 = 1
print(count_pairs(nums1, k1))  
print(count_pairs(nums2, k2)) 