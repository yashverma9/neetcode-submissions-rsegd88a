class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupsDict = {}
        for num in nums:
            if num in dupsDict:
                dupsDict[num] += 1
            else:
                dupsDict[num] = 1
        for count in dupsDict.values():
            if count > 1:
                return True

        return False