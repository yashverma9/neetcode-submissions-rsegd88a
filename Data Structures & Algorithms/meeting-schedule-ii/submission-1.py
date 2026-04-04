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

        s = e = 0
        count = 0
        res = 0

        while s < len(start):
            if start[s] < end[e]:
                count += 1 # New Meeting room occupied
                s += 1
            else:
                count -= 1 # Meeting room free
                e += 1
        
            if count > res:
                res = count
        
        return res