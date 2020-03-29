# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    def rob(self, root: TreeNode) -> int:
        def helper(node):
            if not node:
                return [0, 0]
            l = helper(node.left)
            r = helper(node.right)
            return [node.val + l[1] + r[1], max(l)+max(r)]
        return max(helper(root))


class Solution2:
    def __init__(self):
        self.memo = {}

    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root in self.memo:
            return self.memo[root]

        v_withRoot = root.val + self.rob_withoutRoot(root.left) + self.rob_withoutRoot(root.right)
        v_withoutRoot = self.rob_withoutRoot(root)
        self.memo[root] = max(v_withRoot, v_withoutRoot)
        return max(v_withRoot, v_withoutRoot)

    def rob_withoutRoot(self, root):
        if not root:
            return 0
        if root.left in self.memo:
            l = self.memo[root.left]
        else:
            l = self.rob(root.left)
            self.memo[root.left] = l

        if root.right in self.memo:
            r = self.memo[root.right]
        else:
            r = self.rob(root.right)
            self.memo[root.right] = r
        return (l + r)

## 213. House Robber II

class Solution0:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        return max(self.rob_nocircle(nums[0:-1]), self.rob_nocircle(nums[1:-2]) + nums[-1])

    def rob_nocircle(self, nums):  ## space and time - O(N)
        if not nums:
            return 0

        dp = [0] * len(nums)
        dp[0] = nums[0]
        if len(nums) >= 2:
            dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]