class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def backspace(strng):
            ans = []
            for c in strng:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        
        return backspace(S) == backspace(T)