class MinStack: 
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []

    def push(self, val: int) -> None:
        self.arr.append(val)        

    def pop(self) -> None:
        self.arr.pop()        

    def top(self) -> int:
        return self.arr[-1]        

    def getMin(self) -> int:
        return min(self.arr)
        

# 2nd way of doing
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()