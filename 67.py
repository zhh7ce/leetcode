#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m = len(a)
        n = len(b)
        ans = [0] * max(m, n)
        for i in range(-1, -m-1, -1):
            if a[i] == '1':
                ans[i] += 1
        for i in range(-1, -n-1, -1):
            if b[i] == '1':
                ans[i] += 1
        print(ans)
        for i in range(-1, -len(ans), -1):
            if ans[i] > 1:
                ans[i] %= 2
                ans[i-1] += 1
        if ans[0] > 1:
            ans[0] %= 2
            ans.insert(0, 1)
        for i in range(len(ans)):
            ans[i] = str(ans[i])
        return ''.join(ans)

# @lc code=end

s = Solution()
print(s.addBinary("1010", "1011"))

