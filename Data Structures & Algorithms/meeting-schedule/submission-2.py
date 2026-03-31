"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        for i,j in enumerate(intervals):
            if j.start > j.end:
                return False
            if (i-1) >= 0:
                # print(intervals[i-1].end,  intervals[i].start)
                if intervals[i-1].end > intervals[i].start:
                    return False

        return True
