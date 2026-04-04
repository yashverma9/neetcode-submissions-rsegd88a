class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Optimal - Time - O(n*2^n) - similar to subset, as again we either pick a number or skip it
        # There is no reuse of same index candidate
        # Space - O(n) without output (depth), with - O(n* 2^n) due 2^n subsets possible
        '''
        We sort initially to avoid duplicates later, every possible path we check if the
        value is not duplicate as previously used. If same then skip, otherwise check combination.

        As we either pick a number or skip, its 2 choices like subset question. We also break, when
        the sum exceeds target and there is no need to check that combinatino there onwards.
        '''
        candidates.sort()

        res = []
        n = len(candidates)

        def calSum(index, sum, comb):
            if sum == target:
                res.append(comb[:])
                return
            
            if index == n or sum > target:
                return
            
            for i in range(index, n):
                candidate = candidates[i]
                if i != index and candidate == candidates[i-1]:
                    continue
                # As its sorted, any candidate after that is no point checking
                if sum + candidate > target:
                    break
                comb.append(candidate)
                calSum(i + 1, sum + candidate, comb)
                comb.pop()
        
        calSum(0, 0, [])

        return res
        