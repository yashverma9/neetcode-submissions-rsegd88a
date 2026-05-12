import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Brute
        maxPile = 0
        for pile in piles:
            maxPile = max(maxPile, pile)

        res = float('inf')
        l = 1
        r = maxPile
        while l <= r:
            rate = l + (r-l)//2

            t = 0
            for pile in piles:
                t += math.ceil(pile/rate)

            if t <= h:
                res = min(res, rate)
                r = rate - 1

            else:
                l = rate + 1
        return res

