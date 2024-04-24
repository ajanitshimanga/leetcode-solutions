class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = nums[0]
        max_so_far = nums[0]
        for num in nums[1:]:
            curr_max = max(num, curr_max + num)
            max_so_far = max(max_so_far, curr_max)
        return max_so_far
