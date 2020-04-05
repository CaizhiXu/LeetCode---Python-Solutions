"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""


## time, space - O(E+V)
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        visited = {}
        visited[node] = Node(node.val)
        self.dfs(node, visited)
        return visited[node]

    def dfs(self, node, visited):
        for nei in node.neighbors:
            if nei not in visited:
                visited[nei] = Node(nei.val)
                self.dfs(nei, visited)
            visited[node].neighbors.append(visited[nei])