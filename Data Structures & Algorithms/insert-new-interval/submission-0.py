class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Brute
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


            
