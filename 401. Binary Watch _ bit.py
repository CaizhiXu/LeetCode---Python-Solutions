## time, space - O(10**n)
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        def dfs(n, hour, minu, idx):
            if hour>11 or minu>59:
                return
            if n == 0:
                res.append(str(hour) + ":"+ "0"*(minu<10) + str(minu))
                return
            for i in range(idx, 10):
                if i<4:
                    dfs(n-1, hour|1<<i, minu, i+1)
                else:
                    dfs(n-1, hour, minu|1<<(i-4), i+1)
        res = []
        dfs(num, 0, 0, 0)
        return res