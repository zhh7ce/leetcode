#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#
from typing import List
# @lc code=start
class Solution:
    hours = [8, 4, 2, 1]
    mintues = [32, 16, 8, 4, 2, 1]
    def readBinaryWatch(self, num: int) -> List[str]:
        empty = [0] * 10
        leds = [empty]
        counts = [0]
        ends = [0]
        array = []
        while leds:
            led = leds.pop()
            count = counts.pop()
            end = ends.pop()
            if count == num:
                array.append(led)
                continue
            for i in range(end, 10):
                tmp = led.copy()
                tmp[i] = 1
                if self.isLegal(tmp):
                    leds.append(tmp)
                    counts.append(count+1)
                    ends.append(i+1)
        time = []
        for led in array:
            hour = 0
            for i in range(4):
                if led[i]:
                    hour += self.hours[i]
            minute = 0
            for i in range(6):
                if led[4+i]:
                    minute += self.mintues[i]
            string = str(hour)
            string += ':'
            if minute < 10:
                string += '0'
            string += str(minute)
            time.append(string)
        return time               

    def isLegal(self, led):
        hour = 0
        for i in range(4):
            if led[i]:
                hour += self.hours[i]
        if hour > 11:
            return False

        minute = 0
        for i in range(6):
            if led[4+i]:
                minute += self.mintues[i]
        if minute > 59:
            return False
        return True
# @lc code=end

s = Solution()
print(s.readBinaryWatch(1))