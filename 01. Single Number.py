class Solution:
    def singleNumber(self, nums: List[int]):
        no_duplicate = []
        for num in nums:
            if num not in no_duplicate:
                no_duplicate.append(num)
            else:
                no_duplicate.remove(num)
            
        return no_duplicate.pop()