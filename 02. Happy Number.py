class Solution:
    def isHappy(self, n: int) -> bool:
        
        def square_sum(num):
            rem = 0
            sum_n = 0
            while num>0:
                rem = num%10
                sum_n += (rem*rem)
                num = num//10
            return sum_n
        
        seen = set()
            
        while square_sum(n) not in seen:
            
            sum1 = square_sum(n)
            if sum1 == 1:
                return True
            else:
                n = sum1
                seen.add(sum1)
        return False