class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # optimal

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False