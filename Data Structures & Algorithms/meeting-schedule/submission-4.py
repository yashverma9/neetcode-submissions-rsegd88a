"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Brute O(n2)
        # Check for each interval
        for i in range(len(intervals)):
            prev = intervals[i]
            for j in range(len(intervals)):
                cur = intervals[j]
                if i != j:
                    if prev.end > cur.start and cur.end > prev.start:
                        return False
        return True