class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Optimal

        intervals.sort()

        count = 0

        prev = intervals[0]

        for i in range(1, len(intervals)):
            cur = intervals[i] 

            # Means overlap
            if prev[0] < cur[1] and prev[1] > cur[0]:
                count += 1
                if prev[1] > cur[1]:
                    prev = cur
            else:
                prev = cur
        return count