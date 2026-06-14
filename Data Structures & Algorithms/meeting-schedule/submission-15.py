"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True
        intervals.sort(key = lambda x : x.start)
        obj = intervals[0]
        for curr in intervals[1:]:
            if curr.start < obj.end:
                return False
            else:
                obj = curr

        return True
