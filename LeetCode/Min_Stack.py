# https://leetcode.com/problems/min-stack/
import math

class MinStack:
    def __init__(self):
        self.stack = [(0, math.inf)]

    def push(self, val: int) -> None:
        self.stack.append((val, min(self.stack[-1][1], val)))

    def pop(self) -> None:
        self.stack.pop(-1)
    
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())   # return -3
minStack.pop()
print(minStack.top())      # return 0
print(minStack.getMin());  # return -2

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
