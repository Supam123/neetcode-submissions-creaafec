class MinStack:

    def __init__(self):
        self.values = []

    def push(self, val: int) -> None:
        if len(self.values) == 0:
            self.values.append((val,val))
        else:
            if val < self.values[-1][1]:
                mini = val
                self.values.append((val,mini))
            else:
                mini = self.getMin()
                self.values.append((val,mini))
        return
                
        

    def pop(self) -> None:
        return self.values.pop()
        

    def top(self) -> int:
        return self.values[-1][0]
        

    def getMin(self) -> int:
        return self.values[-1][1]
        
