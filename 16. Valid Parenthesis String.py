class Solution:
    def checkValidString(self, s: str) -> bool:
        if len(s) == 0 or s == "*":
            return True
        if len(s) == 1:
            return False
        
        left = 0
        for item in s:
            if item == ')':
                left -= 1
            else:
                left += 1
        
            if left < 0:
                return False
            
        if left == 0:
            return True
        
        right = 0
        for item in reversed(s):
            if item == '(':
                right -= 1
            else:
                right += 1
        
            if right < 0:
                return False
        
        return True
    
    
    
# class Solution:
#     def checkValidString(self, s: str) -> bool:
#         openst = []
#         special = []
        
#         for i in range(len(s)):
#             c = s[i]
#             if c == '(':
#                 openst.append(i)
#             elif c == '*':
#                 special.append(i)
#             elif c == ')':
#                 if openst:
#                     openst.pop()
#                 elif special:
#                     special.pop()
#                 else:
#                     return False
#             else:
#                 return False
#         print(openst, special)
#         while (openst and special):
#             if openst[-1] > special[-1]:
#                 return False 
#             openst.pop()
#             special.pop()
#         return len(openst) == 0