from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for dep, arr in tickets:
            graph[dep].append(arr)
        num_tick = len(tickets)

        def dfs(start, itinerary, num_tick):
            if len(itinerary) == num_tick:
                return itinerary + [start]
            if start not in graph:
                return None
            for next_city in sorted(graph[start]):
                graph[start].remove(next_city)
                temp = dfs(next_city, itinerary + [start], num_tick)
                if temp:
                    return temp
                graph[start].append(next_city)
            return None

        return dfs('JFK', [], num_tick)
