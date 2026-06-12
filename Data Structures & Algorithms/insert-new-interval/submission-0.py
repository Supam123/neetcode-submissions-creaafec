class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: # if the new interval ends before the current interval even starts
                res.append(newInterval)
                return  res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i]) # safely place my current interval 
                # not appending new interval cuz it mnight overlap inn future
            else:
                newInterval[0] = min(newInterval[0],intervals[i][0])
                newInterval[1] = max(newInterval[1],intervals[i][1])
                # we merged them and we dont append cuz it again it moght over lap with someting in futurre
        res.append(newInterval)
        return res