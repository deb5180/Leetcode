class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        for item in arr:
            if item+1 in arr:
                count += 1

        return count