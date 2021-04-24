class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {}
        max_subarray = 0
        count = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
        
            if count not in dic:
                dic[count] = i
            else:
                max_subarray = max(max_subarray, i-dic[count])

            if count == 0:
                max_subarray = i+1
            
        return max_subarray