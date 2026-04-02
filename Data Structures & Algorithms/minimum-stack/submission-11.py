class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val,val))
        else:
            curr_mini = self.getMin()
            if val < curr_mini:
                self.stack.append((val,val))
            else:
                self.stack.append((val,curr_mini))

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
