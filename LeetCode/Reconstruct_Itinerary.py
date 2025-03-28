# https://leetcode.com/problems/reconstruct-itinerary/

from collections import defaultdict
from typing import List
import copy


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(airport: str):
            while start_end_ticket_map[airport]:
                next_airport = start_end_ticket_map[airport].pop()
                dfs(next_airport)
            route.append(airport)

        start_end_ticket_map = defaultdict(list)
        for ticket in tickets:
            start_end_ticket_map[ticket[0]].append(ticket[1])

        for airport in start_end_ticket_map:
            start_end_ticket_map[airport].sort(reverse=True)

        route = []

        dfs("JFK")
        return route[::-1]


tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Output = ["JFK", "MUC", "LHR", "SFO", "SJC"]
tickets = [
    ["EZE", "TIA"],
    ["EZE", "HBA"],
    ["AXA", "TIA"],
    ["JFK", "AXA"],
    ["ANU", "JFK"],
    ["ADL", "ANU"],
    ["TIA", "AUA"],
    ["ANU", "AUA"],
    ["ADL", "EZE"],
    ["ADL", "EZE"],
    ["EZE", "ADL"],
    ["AXA", "EZE"],
    ["AUA", "AXA"],
    ["JFK", "AXA"],
    ["AXA", "AUA"],
    ["AUA", "ADL"],
    ["ANU", "EZE"],
    ["TIA", "ADL"],
    ["EZE", "ANU"],
    ["AUA", "ANU"],
]
# Output = ["JFK", "AXA", "AUA", "ADL", "ANU", "AUA", "ANU", "EZE", "ADL", "EZE", "ANU", "JFK", "AXA", "EZE", "TIA", "AUA", "AXA", "TIA", "ADL", "EZE", "HBA"]
tickets = [
    ["JFK", "AAA"],
    ["AAA", "BBB"],
    ["BBB", "CCC"],
    ["AAA", "EEE"],
    ["EEE", "JFK"],
    ["JFK", "AAA"],
]
# Output = ['JFK', 'AAA', 'EEE', 'JFK', 'AAA', 'BBB', 'CCC']
solution = Solution()
print(solution.findItinerary(tickets))

import math
