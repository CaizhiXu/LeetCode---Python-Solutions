## time - O(N*N)
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def minmax(s, e, turn, memo):
            if s == e:
                return nums[s] * turn
            if (s, e) in memo:
                return memo[(s, e)]
            left = nums[s] * turn + minmax(s + 1, e, -1 * turn, memo)
            right = nums[e] * turn + minmax(s, e - 1, -1 * turn, memo)
            if turn > 0:
                ans = max(left, right)
            else:
                ans = min(left, right)

            memo[(s, e)] = ans
            return ans

        memo = {}
        return True if (minmax(0, len(nums) - 1, 1, memo) >= 0) else False
