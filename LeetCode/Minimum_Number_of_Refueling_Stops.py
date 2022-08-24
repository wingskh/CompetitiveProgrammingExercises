# https://leetcode.com/problems/minimum-number-of-refueling-stops/
# https://leetcode.com/problems/minimum-number-of-refueling-stops/discuss/2452673/python-easily-understood-faster-than-90-fast
import heapq


class Solution:
    def minRefuelStops(
        self, target: int, startFuel: int, stations: List[List[int]]
    ) -> int:
        cur_fuel = startFuel
        missed_fuel = []
        heapq.heapify(missed_fuel)
        stations.append([target, 0])
        refuel_count = 0
        prev_location = 0

        for station in stations:
            cur_fuel -= station[0] - prev_location
            while cur_fuel < 0:
                if len(missed_fuel) == 0:
                    return -1
                    
                cur_fuel -= heapq.heappop(missed_fuel)
                refuel_count += 1
            heapq.heappush(missed_fuel, -station[1])
            prev_location = station[0]

        return refuel_count


target = 100
startFuel = 10
stations = [[10, 60], [20, 30], [30, 30], [60, 40]]
target = 100
startFuel = 1
stations = [[10,100]]
sol = Solution()
print(sol.minRefuelStops(target, startFuel, stations))
