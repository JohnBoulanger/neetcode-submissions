class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        start = 0
        diff = 0
        for i in range(len(gas)):
            diff += (gas[i] - cost[i])
            tank += (gas[i] - cost[i])
            # if weve run out of gas, the previous start station and any stations until i are not possible
            # because starting at start or any in between will get an empty tank at i
            # try starting one further ahead and reset the tank
            if tank < 0:
                bestTank = tank
                start = i + 1
                tank = 0

        if diff < 0 or start == len(gas):
            return -1
        
        return start
            