#
# @lc app=leetcode.cn id=738 lang=python3
#
# [738] 单调递增的数字
#

# @lc code=start
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        n = N
        array = []
        while n > 0:
            array.append(n % 10)
            n //= 10
        n = len(array)
        array.reverse()
        equal = [False] * n
        for i in range(n-1):
            if array[i] == array[i+1]:
                equal[i+1] = True
            elif array[i] > array[i+1]:
                for j in range(i+1, n):
                    array[j] = 9
                for j in range(i, -1, -1):
                    if equal[j]:
                        array[j] = 9
                    else:
                        array[j] -= 1
                        answer = 0
                        for i in array:
                            answer *= 10
                            answer += i
                        return answer
        return N
# @lc code=end
s = Solution()
print(s.monotoneIncreasingDigits(10000))

