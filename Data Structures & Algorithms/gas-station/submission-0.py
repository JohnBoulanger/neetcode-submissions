class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        start = 0
        for i in range(len(gas)):
            tank += (gas[i] - cost[i])
            # if weve run out of gas, the previous start station and any stations until i are not possible
            # because starting at start or any in between will get an empty tank at i
            # try starting one further ahead and reset the tank
            if tank < 0:
                bestTank = tank
                start = i + 1
                tank = 0

        
        # no start point was found in first pass
        if start == len(gas):
            return -1

        # check if its possible to do a loop from start
        tank = 0
        for i in range(start, len(gas)):
            tank += (gas[i] - cost[i])
        for i in range(0, start):
            tank += (gas[i] - cost[i])

        if tank < 0:
            return -1
        
        return start
            