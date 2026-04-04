class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
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