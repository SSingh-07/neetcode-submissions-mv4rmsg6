"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        res, curr = 0, 0
        length = len(end)

        s, e = 0, 0
        flag = 0

        while e<length:
            if start[s] < end[e] and flag == 0:
                curr +=1
                res = max(res, curr)
                if s < length -1:
                    s+=1
                else:
                    flag = 1

            else:
                curr-=1
                e+=1

        return res

            



        