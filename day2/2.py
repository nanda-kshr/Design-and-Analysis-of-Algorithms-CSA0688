def rob_houses(nums):
    def rob_linear(nums):
        prev, curr = 0, 0
        for num in nums:
            prev, curr = curr, max(curr, prev + num)
        return curr
    return max(nums[0], rob_linear(nums[1:]), rob_linear(nums[:-1])) if len(nums) != 1 else nums[0]
print(rob_houses([2, 3, 2]))
print(rob_houses([1, 2, 3, 1]))