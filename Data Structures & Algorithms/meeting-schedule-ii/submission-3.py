"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        startTimes =sorted(x.start for x in intervals)
        endTimes =  sorted(x.end for x in intervals)
        i,j=0,0
        count = 0
        largest = 0
        while i < len(intervals):
            s = startTimes[i]
            e = endTimes[j]
            if s < e:
                count += 1
                i += 1
            else:
                j+=1
                count -= 1
            largest = max(count,largest)
        return largest




























        