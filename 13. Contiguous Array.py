class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_n = 0
        dic = {}
        dic[0] = -1
        subarray_len = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                sum_n -= 1
            else:
                sum_n += 1
            
            if sum_n not in dic:
                dic[sum_n] = i
            else:
                subarray_len = max(subarray_len, i-dic[sum_n])
                
        return subarray_len