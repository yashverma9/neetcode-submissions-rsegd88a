class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # BRUTE

        for start in range(len(gas)):
            tank = gas[start]
            curCost = cost[start]
            tank = tank - curCost
            if tank < 0:
                continue

            station = 0 if start == len(gas) - 1 else start + 1

            while station != start: 
                tank = tank + gas[station] - cost[station]
                if tank < 0:
                    break

                station = 0 if station == len(gas) - 1 else station + 1
            
            if station == start:
                return start
        
        return -1
            