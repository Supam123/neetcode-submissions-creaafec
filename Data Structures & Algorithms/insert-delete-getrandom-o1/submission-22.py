class RandomizedSet:

    def __init__(self):
        self.h = {}
        self.l = []

    def insert(self, val: int) -> bool:
        if val not in self.h:
            self.h[val] = len(self.l)
            self.l.append(val)
            return True
        else:
            return False

        

    def remove(self, val: int) -> bool:
        if val in self.h:
            idx =  self.h[val]
            last = self.l[-1]
            self.l[idx] = last
            self.l.pop()
            self.h[last] = idx
            del self.h[val]
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        return random.choice(self.l)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()