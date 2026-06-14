"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startT =sorted(x.start for x in intervals)
        endT =  sorted(x.end for x in intervals)
        count = 0
        largest = 0
        i,j  = 0,0
        while i < len(intervals):
            if startT[i] < endT[j]:
                count += 1
                i+=1
            else:
                count -= 1
                j += 1
            largest = max(largest,count)
        return largest
        