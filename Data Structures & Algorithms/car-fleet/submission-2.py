class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0

        # time to destination = (target - position) / speed
        # sorted by starting position increasing
        pairs = sorted([(d, v) for d, v in zip(position, speed)], key=lambda p: p[0])
        timeToDest = [(target - d) / v for d, v in pairs]


        # cars with ttd less than timeToDest[-1] will be stuck behind the leader when they
        # arrive in a fleet, so pop them all together and fleet += 1
        while timeToDest:
            leader = timeToDest[-1]
            while timeToDest and timeToDest[-1] <= leader:
                timeToDest.pop()

            fleets += 1
    
        return fleets