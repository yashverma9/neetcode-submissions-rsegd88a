class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Optimal- O(nlogn), O(n) due to sort, O(1) otherwise
        '''
        We sort the intervals, just check for overlap between a prev and cur
        If overlap, we increment count and keep the interval with small end time
        because it leaves more space for future interval (least removals eventually)

        So prev is updated with cur only if cur has smaller end time in overlap or if
        there is no overlap
        '''
        intervals.sort()

        count = 0

        prev = intervals[0]

        for i in range(1, len(intervals)):
            cur = intervals[i] 

            # Means overlap prev[0] < cur[1] and prev[1] > cur[0]
            # Can be reduced to this only because sorted
            if prev[1] > cur[0]:
                count += 1
                # We want to keep interval with smaller end to give future intervals more space
                if prev[1] > cur[1]:
                    prev = cur
            else:
                prev = cur
        return count