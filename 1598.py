#
# @lc app=leetcode.cn id=1598 lang=python3
#
# [1598] 文件夹操作日志搜集器
#

# @lc code=start
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        deepth = 0
        for i in logs:
            if i == '../':
                if deepth > 0:
                    deepth -= 1
                continue
            if i == './':
                continue
            deepth += 1
        return deepth
# @lc code=end

