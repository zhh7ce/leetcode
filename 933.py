#
# @lc app=leetcode.cn id=933 lang=python3
#
# [933] 最近的请求次数
#

# @lc code=start
class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        self.queue.append(t)
        n = len(self.queue)
        m = 0
        for i in range(n):
            if t - self.queue[0] > 3000:
                self.queue.pop(0)
                m += 1
            else:
                break
        return n - m


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end

