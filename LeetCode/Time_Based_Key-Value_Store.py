# https://leetcode.com/problems/time-based-key-value-store/
import math


class TimeMap:
    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap or timestamp < self.hashmap[key][0][1]:
            return ""

        if timestamp > self.hashmap[key][-1][1]:
            return self.hashmap[key][-1][0]
        
        left_index, right_index = 0, len(self.hashmap[key]) - 1

        while left_index < right_index:
            middle_index = left_index + math.ceil((right_index - left_index) / 2)
            middle_value = self.hashmap[key][middle_index][1]
            if middle_value == timestamp:
                left_index = middle_index
                break
            elif middle_value > timestamp:
                right_index = middle_index - 1
            else:
                left_index = middle_index
        
        return self.hashmap[key][left_index][0]

    # def get(self, key: str, timestamp: int) -> str:
    #     if key not in self.hashmap or timestamp < self.hashmap[key][0][1]:
    #         return ""

    #     if timestamp > self.hashmap[key][-1][1]:
    #         return self.hashmap[key][-1][0]
        
    #     left_index, right_index = 0, len(self.hashmap[key]) - 1

    #     while left_index <= right_index:
    #         middle_index = left_index + (right_index - left_index) // 2
    #         middle_value = self.hashmap[key][middle_index][1]
    #         if middle_value == timestamp:
    #             left_index = middle_index
    #             break
    #         elif middle_value > timestamp:
    #             right_index = middle_index - 1
    #         else:
    #             left_index = middle_index + 1
        
    #     if left_index < len(self.hashmap[key])-1:
    #         return self.hashmap[key][left_index][0]
    #     else:
    #         return self.hashmap[key][right_index][0]
        

obj = TimeMap()

operations = ["TimeMap", "set", "get", "get", "set", "get", "get"]
values = [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
answer = [None, None, "bar", "bar", None, "bar2", "bar2"]

# operations = ["TimeMap","set","set","get","get","get","get","get"]
# values = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
# answer = [None,None,None,"","high","high","low","low"]
result = []
for i in range(len(operations)):
    if operations[i] == 'set':
        key,value,timestamp = values[i]
        obj.set(key, value, timestamp)
    elif operations[i] == 'get':
        key,timestamp = values[i]
        result.append(obj.get(key, timestamp))
        continue
    result.append(None)

result
