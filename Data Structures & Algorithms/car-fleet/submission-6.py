class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ### Using stack ###

        # What we can see is that a car will collide and become a fleet with a car
        # that is just next to it. There is no way a car will fleet by skipping a car
        # Consider a car and a car ahead of it. It can only catch the next car if the
        # time to reach target is less than the next car. That makes one fleet.
        # We can push to stack to keep all fleets. We push only when we find a fresh car
        # when its not possible to catch up the next car (time>prevTime)
        # we do this from reverse (start with car nearest to target) and go back down
        # Reason for reverse is because if we start from begining, and 1st 2 cars fleet up
        # We wont know whether the 2nd one might collide later again and its speed might change
        # Still pretty unclear- bs

        fleetStack = []
        cars = list(zip(position,speed)) # Combining both to form a cars tuple iter
        cars.sort(reverse= True)

        for pos, sp in cars:
            time = (target - pos)/sp
            if not fleetStack or time > fleetStack[-1]:
                fleetStack.append(time)
        
        return len(fleetStack)

        

           


