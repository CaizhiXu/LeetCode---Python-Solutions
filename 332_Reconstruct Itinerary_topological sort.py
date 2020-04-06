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


## time - O(E), space - O(V+E)
from collections import defaultdict


class Solution2:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)

        itinerary = ['JFK']
        num_tickets = len(tickets)
        self.backtrack('JFK', graph, itinerary, num_tickets)
        return itinerary

    def backtrack(self, src, graph, itinerary, num_tickets):
        if len(itinerary) == num_tickets + 1:
            return True
        for nei in sorted(graph[src]):
            graph[src].remove(nei)
            itinerary.append(nei)
            if self.backtrack(nei, graph, itinerary, num_tickets):
                return True
            graph[src].append(nei)
            itinerary.pop()
        return False
