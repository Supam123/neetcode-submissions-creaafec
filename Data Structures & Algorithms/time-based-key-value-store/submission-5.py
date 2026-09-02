class TimeMap:

    def __init__(self):
        self.hashmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = [(value,timestamp)]
        else:
            self.hashmap[key].append((value,timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        # we are finding the rightmost timestamp which means record and move right
        # if the timestamp is true we record the answer we get greedy to find the largest
        # so we move right shrink left.
        if key not in self.hashmap:
            return ""
        res = ""
        l = 0
        r = len(self.hashmap[key]) - 1
        while l <= r :
            mid =  (l+r) // 2
            if self.hashmap[key][mid][1] <= timestamp:
                res = self.hashmap[key][mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res
















        
