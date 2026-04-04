class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Brute

        combined = [(position[i],speed[i]) for i in range(len(position))]
        combined.sort()

        fleets = []
        count = 0

        for i in range (len(combined)-1, -1, -1):
            time = (target - combined[i][0])/combined[i][1] # To get ceil div
            
            
            if not fleets or time > fleets[-1]:
                fleets.append(time)
        
        return len(fleets)


                


