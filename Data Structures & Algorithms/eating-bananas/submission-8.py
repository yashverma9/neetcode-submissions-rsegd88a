class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # min k, = 1 , max k = max(piles)
        
        ### Brute force O(n*m) n is len, m is max ###
        # Here we check for all possible values of k,
        # which lies between 1 (min) and max(piles) (maxf)
        # This fails on submitting as bigger test case fail
        # with time limit exceeded.
        # speed = 1
        # while True:
        #     totalTime = 0
        #     for pile in piles:
        #         totalTime += math.ceil(pile / speed)
        #     if totalTime <= h:
        #         return speed
        #     speed += 1
        # return speed


        ### Binary search ###

        # As we were searching for a value thats suits us,
        # and is min out of a range. Hence we can try binary search

        maxK = 0
        for pile in piles:
            maxK = max(maxK, pile)

        l, r = 1, maxK
        speed = 0

        while (l <= r):
            mid = l + ((r-l)//2)
            time = 0
            for pile in piles:
                time += math.ceil(pile/mid)
            if time <= h:
                speed = mid
                r = mid - 1
            else:
                l = mid + 1 
        return speed

