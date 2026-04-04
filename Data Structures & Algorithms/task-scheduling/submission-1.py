class Solution:
    # Brute force
    # O(m*n) worst case, where m is total tasks and n is waiting cycle 
    # The time comp is not just O(m) (based on code) because in case of all identical task we wait (m-1)*n times
    # Hence worst case its order of m*n => O(m*n)
    # Space - O(26) ~ O(1)
    '''
    A CPU will pick task based on these factor:
        - Pick the most frequent task (because if less frequent picked early, we will have many idles later)
        - Pick a task which is possible based on time wait (cycle wait - n)
    
    Hence, we continue iteration till we have tasks left. Every iteration we find out task with maxFreq
    which is possible to process based on nextAvailable hashmap maintained by us

    We decrease its freq if picked for processing, and update the nextAvailable time for that task based
    on the n value (t+n+1)

    In the end every iteration increase time by 1 as either a task was processed or left Idle.
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
        
        # We count on how many seconds taken, in the end an extra second is added which works for us because we start at 0
        return time