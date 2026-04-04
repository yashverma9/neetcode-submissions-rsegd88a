"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Optimal O(nlogn), O(n) for sorting
        # Simply check for over lap with prev meeting
        if not intervals:
            return True
        intervals.sort(key = lambda i : i.start)
        prev = intervals[0]

        for i in range (1, len(intervals)):
            cur = intervals[i]
            # Overlap condition for sorted intervals
            if prev.end > cur.start:
                return False
            prev = cur
        
        return True
        













