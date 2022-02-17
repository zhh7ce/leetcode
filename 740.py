#
# @lc app=leetcode.cn id=740 lang=python3
#
# [740] 删除与获得点数
#

# @lc code=start
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        prev = -1
        sums = 0
        sumsWithoutLast = 0
        dictory = dict()
        for i in nums:
            if i in dictory:
                dictory[i] += 1
            else:
                dictory[i] = 1
        for i in list(dictory.keys()):
            if prev == i-1:
                tmp = sums
                sums = max((sumsWithoutLast + i*dictory[i]), sums)
                sumsWithoutLast = tmp
            else:
                sumsWithoutLast = sums
                sums += i*dictory[i]
            prev = i
        return max(sums, sumsWithoutLast)
        
# @lc code=end

nums = [1,1,1,2,4,5,5,5,6]
sol = Solution()
print(sol.deleteAndEarn(nums))

