class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))

        # create a list of the cars where we sort their order in the array by starting pos
        sortedCars = sorted(cars, key=lambda car: car[0])
        # list of cars[i]'s time to its destination based off its current speed
        timeToDestination = [(target - d) / v for (d, v) in sortedCars]
        fleets = 0
        # go through all arrival times from cars starting with cars
        # that started ahead first
        while timeToDestination:
            t = timeToDestination[-1]
            # if a car behind wouldve reached the destination before the slowest car in front
            # of it, it is part of that fleet, remove it
            while timeToDestination and timeToDestination[-1] <= t:
                timeToDestination.pop()

            # once you find a car that would take longer than all of the cars (incl the slowest)
            # then its the start of a new fleet, add the fleet ahead of it to the total
            fleets += 1

        return fleets