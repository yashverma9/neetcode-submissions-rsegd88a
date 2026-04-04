class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
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
                comb.append(candidate)
                calSum(i + 1, sum + candidate, comb)
                comb.pop()
        
        calSum(0, 0, [])

        return res
        