# https://leetcode.com/problems/car-fleet/
from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        remaining_time = [(target - position[i]) / speed[i] for i in range(len(position))]
        sorted_tuples = sorted(zip(position, remaining_time), key=lambda x: x[0])

        last_max_car_required_time = -1
        num_of_car_fleet = 0
        while len(sorted_tuples) != 0:
            current_car_required_time = sorted_tuples.pop()[1]
            if current_car_required_time > last_max_car_required_time:
                num_of_car_fleet += 1
            last_max_car_required_time = max(current_car_required_time, last_max_car_required_time)

        return num_of_car_fleet


target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
target = 10
position = [0,4,2]
speed = [2,1,3]
target = 100
position = [8,3,7,4,6,5]
speed = [4,4,4,4,4,4]
sol = Solution()
print(sol.carFleet(target, position, speed))


#   target = 12
#   10,     8,      0,      5,      3
#   2,      4,      1,      1,      3
#   1h,     1h,     12h,    6h,     9h,
#   after sorting
#   10,     8,      5,      3,      0
#   2,      4,      1,      3,      1
#   1h,     1h,     6h,      3h,     12h
#         
# 
#   target: 10
#   0       4       2
#   2       1       3
#   5h      6h      3h   
#   after sorting
#   4       2       0
#   1       3       2
#   6h      3h      5h 