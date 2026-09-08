class RandomizedSet:

    def __init__(self):
        self.h = {}
        self.l = []
        

    def insert(self, val: int) -> bool:
        if val in self.h:
            return False
        self.h[val] = len(self.l) 
        self.l.append(val)
        return True        

    def remove(self, val: int) -> bool:
        if val not in self.h:
            return False
        idx = self.h[val] # store the idx of the value i wanna delte 
        last = self.l[-1] # get last value
        self.l[idx] = last # at that idx place this one 
        self.l.pop() # delete last one 
        self.h[last] = idx # store the last one as the old idx of the val
        del self.h[val] # del val from hashmap

        return True

        

    def getRandom(self) -> int:
        return random.choice(self.l)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()