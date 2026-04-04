class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Optimal
        '''
        As we need to look for a speed, we can simply run a range between 1 (lowest rate)
        to max banana in a pile(), why not divide and conquer using binary search
        '''
    
        maxK = 0
        for bananas in piles:
            if bananas > maxK:
                maxK = bananas

        
        left = 1
        right = maxK

        mid = left + (right-left)//2 # mid
        k = maxK

        while(left <= right):
            hoursTaken = 0
            for b in piles:
                hoursTaken += -(-b//mid)

            if hoursTaken <= h:
                right = mid-1
                k = mid
        
            else:
                left = mid+1
            
            mid = left + (right-left)//2
        
        return k
