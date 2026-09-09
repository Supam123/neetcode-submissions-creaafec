class HitCounter:

    def __init__(self):
        self.d = collections.deque()


    def hit(self, timestamp: int) -> None:
        self.d.append(timestamp)


    def getHits(self, timestamp: int) -> int:
        while self.d and self.d[0] <= timestamp-300:
            self.d.popleft()
        return len(self.d)



        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
