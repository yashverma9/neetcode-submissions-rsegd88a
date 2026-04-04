class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Brute O(m*n) m = len of intervals, n = len queries, O(n) for output list
        '''
        We find out the length of each interval where query is, update min every iter.
        Return min for each
        '''

        output = []

        for query in queries:
            minLen = float('inf')
            for i in intervals:
                if i[0] <= query <= i[1]:
                    length = i[1] - i[0] + 1
                    if length < minLen:
                        minLen = length
            if minLen != float('inf'):
                output.append(minLen)
            else:
                output.append(-1)
        
        return output
