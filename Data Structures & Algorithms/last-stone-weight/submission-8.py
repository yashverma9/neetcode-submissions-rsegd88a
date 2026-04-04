class Solution:
    # Brute - using sort, sort everytime you add binary search
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        
        def insert(stone):
            nonlocal stones
            l = 0
            r = len(stones) - 1
            inserted = False
            while (l <= r):
                mid = l + (r-l)//2
                if stone == stones[mid]:
                    inserted = True
                    stones = stones[:mid+1] + [stone] + stones[mid+1:]
                    break
                elif stone < stones[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            if not inserted:
                stones = stones[:r+1] + [stone] + stones[r+1:]

        while len(stones) > 1:
            first = stones.pop()
            second = stones.pop()

            new = first - second

            if new:
                insert(new)
        
        if len(stones):
            return stones[0]
        return 0

                    