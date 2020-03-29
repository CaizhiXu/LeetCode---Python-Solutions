## time - O(N), space - O(N)
class Solution:
    def pathSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        node_map = {}
        for num in nums:
            i = num // 100
            j = (num // 10) % 10
            val = num % 10
            node_map[(i, j)] = val
        curr, self.path = node_map[(1, 1)], 0
        self.dfs((1, 1), curr, node_map)
        return self.path

    def dfs(self, node, curr, node_map):
        i, j = node
        if (i + 1, 2 * j - 1) not in node_map and (i + 1, 2 * j) not in node_map:
            self.path += curr
            return
        for k in [2 * j - 1, 2 * j]:
            if (i + 1, k) in node_map:
                self.dfs((i + 1, k), curr + node_map[(i + 1, k)], node_map)