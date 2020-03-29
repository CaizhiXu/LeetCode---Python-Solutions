# Solution 1 - Kruskal's algo
# time, space - O(NlogN)
class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if size[rootX] < size[rootX]:
                    x, y = y, x
                parent[rootY] = rootX
                size[rootX] += size[rootY]
                return size[rootX]
            return 0

        parent = [i for i in range(N + 1)]
        size = [1] * (N + 1)
        connections.sort(key=lambda x: x[2])

        total = 0
        for a, b, cost in connections:
            if find(a) != find(b):
                temp = union(a, b)
                total += cost
                if temp == N:
                    return total
        return -1



## solution 2, Prim's algo
class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        '''
        Prim's Algorithm:
        1) Initialize a tree with a single vertex, chosen
        arbitrarily from the graph.
        2) Grow the tree by one edge: of the edges that
        connect the tree to vertices not yet in the tree,
        find the minimum-weight edge, and transfer it to the tree.
        3) Repeat step 2 (until all vertices are in the tree).
        '''
        # city1 <-> city2 may have multiple different cost connections,
        # so use a list of tuples. Nested dict will break algorithm.
        G = collections.defaultdict(list)
        for city1, city2, cost in connections:
            G[city1].append((cost, city2))
            G[city2].append((cost, city1))

        queue = [(0, N)]  # [1] Arbitrary starting point N costs 0.
        visited = set()
        total = 0
        while queue and len(visited) < N:  # [3] Exit if all cities are visited.
            # cost is always least cost connection in queue.
            cost, city = heapq.heappop(queue)
            if city not in visited:
                visited.add(city)
                total += cost  # [2] Grow tree by one edge.
                for edge_cost, next_city in G[city]:
                    heapq.heappush(queue, (edge_cost, next_city))
        return total if len(visited) == N else -1