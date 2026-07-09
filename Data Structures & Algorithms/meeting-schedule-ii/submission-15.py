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
        rooms = 0
        i = 0
        s,e=0,0
        ans = 0
        while i  < len(start):
            if start[s] < end[e]:
                s+=1
                rooms+=1
            else:
                rooms -= 1
                e += 1        
            ans =  max(rooms,ans)
            i+=1

        return ans



        













