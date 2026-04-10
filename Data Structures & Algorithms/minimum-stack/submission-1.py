class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        # l=len(self.stack)
        return self.stack[-1]

    def getMin(self) -> int:
        ans = self.stack[0]
        for i in self.stack:
            ans= min(ans, i)
        return ans
        
