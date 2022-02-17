#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.size = 0


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.size += 1
        temp = []
        while self.stack:
            temp.append(self.stack.pop())
        self.stack.append(x)
        while temp:
            self.stack.append(temp.pop())


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.size -= 1
        return self.stack.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.size == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

if __name__ == "__main__":
    s = MyQueue()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    while not s.empty():
        print(s.pop())