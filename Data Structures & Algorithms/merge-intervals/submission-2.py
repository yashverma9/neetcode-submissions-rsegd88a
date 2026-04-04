class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Optimal, O(nlogn), O(n) for output list
        '''
        Just like the insert interval question, we consider each previous interval
        as a new interval to insert. We sort the intervals initially. Now we check
        if a prev is not overlapping with cur then we append to res. If overlap,
        we make prev a combined interval of prev and cur, and evaluate same prev
        with next cur. We keep doing till end and in the end append the last prev
        to res.
        '''
        res = []   
        prev = None
        cur = None

        intervals.sort()

        for i in range(len(intervals)):
            if not prev:
                prev = intervals[i]
                continue
            
            cur = intervals[i]
            
            if prev[1] < cur[0]:
                res.append(prev)
                prev = cur
            else:
                prev = [prev[0], max(prev[1], cur[1])]
        
        res.append(prev)

        return res