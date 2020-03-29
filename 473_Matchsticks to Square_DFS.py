class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if not nums:
            return False
        sideLen = sum(nums) / 4
        if int(sideLen) != sideLen:
            return False
        nums.sort(reverse=True)
        visited = set()

        def dfs(i, curr):
            if curr == sideLen:
                return True

            for k in range(i + 1, len(nums)):
                if k not in visited and curr + nums[k] <= sideLen:
                    visited.add(k)
                    if dfs(k, curr + nums[k]):
                        return True
                    visited.remove(k)
            return False

        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                temp = dfs(i, nums[i])
                if temp == False:
                    return False
        return True


## Brutal force
class Solution2:
    def makesquare(self, nums: List[int]) -> bool:
        if not nums:
            return False
        sideLen = sum(nums) / 4
        if int(sideLen) != sideLen:
            return False

        length = [0] * 4
        length[0] = nums[0]

        def dfs(length, arr):
            if len(arr) == 0:
                if len(set(length)) == 1:
                    return True
                else:
                    return False
            for i in range(len(length)):
                if length[i] + arr[0] <= sideLen:
                    temp = length.copy()
                    temp[i] = length[i] + arr[0]
                    if dfs(temp, arr[1:]):
                        return True
            return False

        return dfs(length, nums[1:])