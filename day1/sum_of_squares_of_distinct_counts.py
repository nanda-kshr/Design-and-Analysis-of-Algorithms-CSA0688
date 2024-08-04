def sum_of_squares_of_distinct_counts(nums):
    total_sum = 0
    for i in range(len(nums)):
        distinct_elements = set()
        for j in range(i, len(nums)):
            distinct_elements.add(nums[j])
            total_sum += len(distinct_elements) ** 2
    return total_sum
nums1 = [1, 2, 1]
nums2 = [1, 1]
print(sum_of_squares_of_distinct_counts(nums1))  # Output: 15
print(sum_of_squares_of_distinct_counts(nums2))  # Output: 3