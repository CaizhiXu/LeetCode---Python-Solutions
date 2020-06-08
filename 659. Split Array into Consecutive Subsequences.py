## time - O(n), space - O(1)
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        if not nums:
            return False
        i = 0
        pre = None
        lenCnt = [0] * 3
        while i < len(nums):
            tmp = [i for i in lenCnt]
            curr = nums[i]
            cnt = 0
            while i < len(nums) and nums[i] == curr:
                cnt += 1
                i += 1

            if pre == None:
                lenCnt[0] = cnt
            elif pre == curr - 1:
                if cnt < lenCnt[0] + lenCnt[1]:
                    return False
                lenCnt[0] = max(0, cnt - sum(tmp))
                lenCnt[1] = tmp[0]
                lenCnt[2] = tmp[1] + min(tmp[2], cnt - tmp[0] - tmp[1])
            else:
                if lenCnt[0] or lenCnt[1]:
                    return False
                lenCnt[2] = 0
                lenCnt[0] = cnt
            pre = curr

        if lenCnt[0] or lenCnt[1]:
            return False
        else:
            return True