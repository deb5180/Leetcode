class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        curr_sum = nums[0]
        result = nums[0]
        
        for index in range(1, len(nums)):
            curr_sum = max(nums[index], curr_sum+nums[index])
            result = max(curr_sum, result)
            
        return result