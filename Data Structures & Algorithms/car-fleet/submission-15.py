class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Optimal using stack
        '''
            We need to do it in reverse order because a car speed is limited by the car in front of it
            So consider a scenario where 3 cars are there in order A,B,C -> Target, After finding their
            times, we see A reaches in 1.5, B in 1s, C in 2s. So, if see from front now, A can't catchup
            with B and B can catchup with C, so we have 2 fleets. But, technically from behind, 
            B catches up with C and is restricted by C speed now, then A can catchup with C speed
            Hence, 1 fleet. So, from front we need to assume it can't catch, but better to see from restrictive side
        '''
        combined = [(position[i],speed[i]) for i in range(len(position))]
        combined.sort()

        fleets = []
        count = 0

        for i in range (len(combined)-1, -1, -1):
            time = (target - combined[i][0])/combined[i][1] # To get ceil div
            
            
            if not fleets or time > fleets[-1]:
                fleets.append(time)
        
        return len(fleets)


                


