class MinStack:

    def __init__(self):
        self.values = []
        

    def push(self, val: int) -> None:
        if not self.values:
            min_far = val
            self.values.append((val,min_far))
        else:
            min_far = self.getMin()
            if val < min_far:
                min_far = val
                self.values.append((val,min_far))
            else:
                self.values.append((val,min_far))
        

    def pop(self) -> None:
        self.values.pop()
        

    def top(self) -> int:
        return self.values[-1][0]
        

    def getMin(self) -> int:
        return self.values[-1][1]
        
