#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start

class Ugly():
    def __init__(self):
        self.array = [1] * 1690
        p2 = 0
        p3 = 0
        p5 = 0
        for i in range(1, 1690):
            self.array[i] = min(2*self.array[p2], 3*self.array[p3], 5*self.array[p5])
            if 2 * self.array[p2] == self.array[i]:
                p2 += 1
            if 3 * self.array[p3] == self.array[i]:
                p3 += 1
            if 5 * self.array[p5] == self.array[i]:
                p5 += 1

class Solution:
    u = Ugly()
    def nthUglyNumber(self, n: int) -> int:
        return self.u.array[n-1]

# @lc code=end
sol = Solution()
print(sol.nthUglyNumber(110))
