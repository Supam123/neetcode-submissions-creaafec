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
        count = 0
        ans = 0
        s,e=0,0
        for i in range(len(intervals)):
            if start[s] < end[e]:
                count += 1
                s+=1
            else:
                count -= 1
                e+=1
            ans =  max(count,ans)
        return ans
            
        

        