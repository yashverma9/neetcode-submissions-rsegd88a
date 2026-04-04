class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Using iteration
        '''
            Instead of storing the times in a stack, we can just track the bigger time like top 
            of stack and keep count of fleets
        '''
        comb = [(position[i], speed[i]) for i in range(len(position))]

        comb.sort(reverse= True)
        
        prevTime = (target - comb[0][0])/comb[0][1]
        fleets = 1
        for car in comb:
            curTime = (target - car[0])/car[1]
            if curTime > prevTime:
                fleets += 1
                prevTime = curTime

        return fleets
