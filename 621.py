#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] 任务调度器
#
from typing import List
# @lc code=start
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dictory = dict()
        for i in tasks:
            if i in dictory:
                dictory[i] -= 1
            else:
                dictory[i] = -1
        q1 = []
        for i in dictory.values():
            heapq.heappush(q1, i)
        count = 0
        while q1:
            # print(q1)
            q2 = []
            for i in range(n+1):
                if q1:
                    x = heapq.heappop(q1)
                    if x != -1:
                        q2.append(x+1)
                else:
                    if not q2:
                        return count
                count += 1
            for i in q2:
                heapq.heappush(q1, i)
        return count
# @lc code=end
tasks = ["A","A","A","B","B","B","C"]
n = 2
s = Solution()
print(s.leastInterval(tasks, n))
