"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start =sorted(x.start for x in intervals)
        end=  sorted(x.end for x in intervals)
        s,e=0,0
        count = 0
        ans = 0
        for i in range(len(intervals)):
            if start[s] < end[e]:
                s+=1
                count+=1
            else:
                e+=1
                count -=1
            ans =  max(count,ans)
        return ans
            
