def count_indices(nums1, nums2):
    answer1 = sum(1 for i in nums1 if i in nums2)
    answer2 = sum(1 for i in nums2 if i in nums1)
    return [answer1, answer2]
nums1 = [2, 3, 2]
nums2 = [1, 2]
print(count_indices(nums1, nums2))  
nums1 = [4, 3, 2, 3, 1]
nums2 = [2, 2, 5, 2, 3, 6]
print(count_indices(nums1, nums2))  