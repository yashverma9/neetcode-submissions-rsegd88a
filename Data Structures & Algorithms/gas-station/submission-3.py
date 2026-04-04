class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Optimal 
        '''
        One thing we can say for sure is that total gas - total cost should be equal to or
        greater than 0. Otherwise a solution doesnt exist. 

        We can keep track of gas and cost difference at each start point. We keep total
        difference from each start point, if our total ever becomes negative, we reset it
        to 0 and shift start to next station. If we reach the end of array with >= 0 total, 
        we have found our start. We shift directly to i+1 ignoring all stations as start
        b/w the previous start and i is because they will bring the total below 0 at any
        start b/w them. Consider k b/w old start -> i, if its considered a start. Now we know
        till k-1 our total >=0 otherwise we would reset before. So, that means k is going
        to bring us down and so on. Hence, no point checking them.
        
        We don't need to cycle back because there exists only 1 solution. 
        We only need to find a starting point where the journey never dips below zero once 
        — the total sum condition takes care of the rest.
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
        
