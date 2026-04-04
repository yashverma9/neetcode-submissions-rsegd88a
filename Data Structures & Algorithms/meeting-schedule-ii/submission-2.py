"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Optimal - using 2 pointers, O(nlogn), O(n)
        '''
        We divide the intervals into 2 different lists of sorted start and end times 
        We iterate over start when the start time is less than the current end time
        and iterate end if end time is less than start or equal. When start is less
        than end, it means a new meeting overlaps previous end times and hence it
        needs a new room. So we increment count by 1. We decrease count by 1 when
        a room is emptied, thats when start is equal or more than the end time. 

        We update max count seen at every iteration. Basically we are iterating time
        using start and end times and keeping count of rooms occupied
        '''
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