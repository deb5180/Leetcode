class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        move_left = 0
        len_str = len(s)
        for dir, amount in shift:
            if dir == 0:
                move_left += amount
            else:
                move_left -= amount
        move_left = move_left%len_str

        return s[move_left:]+s[:move_left]