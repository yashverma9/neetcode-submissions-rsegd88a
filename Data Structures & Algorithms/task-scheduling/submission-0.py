class Solution:
    # Brute force
    '''
    - Pick the most frequent task
    - Pick a task
    '''
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {} 
        nextAvailable = {} # task: time available at (based on waiting for n cycles/seconds)
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
            nextAvailable[task] = 0 # Done again again, but can be done in another loop

        time = 0

        while sum(freq.values()) > 0:
            taskToProcess = None
            maxFreq = 0

            for task in freq:
                if freq[task] > 0 and nextAvailable[task] <= time:
                    if freq[task] > maxFreq:
                        maxFreq = freq[task]
                        taskToProcess = task
            
            if taskToProcess:
                freq[taskToProcess] -= 1
                # This task can be again processed only after n cycles, hence (t+n+1)th time
                nextAvailable[taskToProcess] = time + n + 1 
            
            time += 1
        
        return time