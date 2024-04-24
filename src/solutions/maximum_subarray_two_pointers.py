class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = nums[0]
        max_so_far = nums[0]
        
        left = 0
        right = 1
        while left < len(nums):
            while right < len(nums):
                nextNum = nums[right]
                if curr_max + nextNum > nextNum:
                    curr_max = curr_max + nextNum
                else:
                    left = right
                    curr_max = nextNum
                max_so_far = max(max_so_far, curr_max)
                    
                right += 1
            left += 1
        return max_so_far
