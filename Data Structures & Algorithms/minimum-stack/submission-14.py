class MinStack:

    def __init__(self):
        self.stack = []
        self.min_so_far = float('-inf')

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.min_so_far = val
            self.stack.append((val,self.min_so_far))
        else:
            mini = self.getMin()
            if val < mini:
                self.min_so_far = val
                self.stack.append((val,self.min_so_far))
            else:
                self.stack.append((val,mini))
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
