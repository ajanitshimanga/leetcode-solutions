class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = dict() # or a set. Pretty confident of it being a dictionary because we need indexes
        for curr_ind in range(len(nums)):
            curr_value = nums[curr_ind]
            desired_value = target - curr_value
            if desired_value in cache:
                desired_index = cache[desired_value]
                return [curr_ind, desired_index]
            cache[curr_value] = curr_ind
        # Time complexity: O(N) because we iterate through the array once, where N is the number of elements in nums. Each lookup also happens in constant time.
        # Space complexity is O(N) because we store at most N pairs of value, indices in a dictionary.
