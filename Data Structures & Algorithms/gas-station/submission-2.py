class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Optimal 
        '''
        One thing we can say for sure is that total gas - total cost should be equal to or
        greater than 0. Otherwise a solution doesnt exist. 

        We can keep track of gas and cost difference at each start point. We keep total
        difference from each start point, if our total ever becomes negative, we reset it
        to 0. If we reach the end of array with >= 0 total, we have found our start.
        
        We don't need to cycle back because there exists only 1 solution, and there is no
        point verifying every step.
        '''

        if sum(gas) - sum(cost) < 0:
            return -1

        total = 0
        start = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                start = i + 1
        
        return start
        
