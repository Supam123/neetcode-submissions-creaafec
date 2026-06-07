class MinStack:

    def __init__(self):
        self.values =[]
        

    def push(self, val: int) -> None:
        self.values.append(val)
        

    def pop(self) -> None:
        if(len(self.values)>0):
            return self.values.pop()
        

    def top(self) -> int:
        if(len(self.values)>0):
            return self.values[-1]
        

    def getMin(self) -> int:
        if(len(self.values)>0):
            return min(self.values)

        
        
