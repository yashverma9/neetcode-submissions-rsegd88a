class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Optimal - linear
        # Time - O(n), space - only for output O(n)

        '''
        Instead of doing in place, we keep adding to res list. If the new interval
        doesnt overlap (new.start > cur.end OR new.end < cur.start), we append
        new to res and return res of intervals appended if new is less than the cur
        or else we just add cur to the res as new could overlap with later intervals

        Now we check overlap with else (new.start <= cur.end AND new.end >= cur.start 
        for closed intervals), and find new interval post making them 
        non overlapping using min of startand max of end. 
        Post exiting loop, we add new interval and return res
        '''
        new = newInterval

        res = []
        for i in range(len(intervals)):
            cur = intervals[i]
            
            if new[1] < cur[0]:
                res.append(new)
                return res + intervals[i:]

            elif cur[1] < new[0]:
                res.append(cur)
            
            #means an overlap
            else:
                new = [min(new[0],cur[0]), max(new[1], cur[1])]
            
        res.append(new)
        return res


            
