class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # arrival = (target - position) / speed
        cars = [[p,s] for p, s in zip(position, speed)]
        cars.sort(key = lambda i: i[0], reverse = True)
        fleets = 0
        fleetarrival = 0

        print(cars)
        for i in cars:
            arrival = (target - i[0]) / i[1]
            if arrival > fleetarrival:
                fleetarrival = arrival
                fleets += 1
            print(arrival, fleets)
        
        return fleets

        # sort the cars in descending order, matching the speed to the indexes

        # iterate through the sorted positions
        # fleet++
        # if arrival time < fleet:
            # don't increment fleet
        # else: fleet++

