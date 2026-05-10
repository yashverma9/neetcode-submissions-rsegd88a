class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Brute  O(n^2), O(n) space
        
        seen = set()

        for num in nums:
            seen.add(num)

        res = 0

        # for num in nums:
        #     count = 1
        #     next = num + 1
        #     while next in seen:
        #         count += 1
        #         next += 1
        #     if count > res:
        #         res = count
        
        # return res

        for num in nums:
            if num-1 not in seen:
                count = 1
                next = num + 1
                while next in seen:
                    count += 1
                    next += 1

                if count > res:
                    res = count 


        return res   
            

        