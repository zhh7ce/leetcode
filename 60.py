#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fac = [1] * n # factrial serise
        num = [0] * n # numbers can be choose
        s = ''
        for i in range(n):
            num[i] = i+1
        for i in range(n-1):
            fac[i+1] = (i+1) * fac[i]
        fac.reverse()
        for i in fac:
            s += str(num.pop((k-1) // i))
            k = k % i 
        return s

# @lc code=end

s = Solution()
print(s.getPermutation(3,3))