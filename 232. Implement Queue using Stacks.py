class MyQueue(object):
    """
    https://leetcode.com/problems/implement-queue-using-stacks/
    """

    def __init__(self):
        self.items = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.items.insert(0, x)

    def pop(self):
        """
        :rtype: int
        """
        return self.items.pop()

    def peek(self):
        """
        :rtype: int
        """
        return self.items[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.items

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()