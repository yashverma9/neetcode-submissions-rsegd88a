class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # STACK

        
        comb = [(position[i], speed[i]) for i in range(len(speed))]
        comb.sort(reverse = True)
        stack = []


        for car in comb:
            if not stack:
                stack.append(car)
                continue
            
            pos, spd = car

            time = (target - pos)/spd

            fleetTime = (target - stack[-1][0]) / stack[-1][1]

            if time <= fleetTime:
                continue
            else:
                stack.append(car)
        
        return len(stack)
