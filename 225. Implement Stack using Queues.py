class MyStack(object):
    """
    https://leetcode.com/problems/implement-stack-using-queues/

    Simply implement a queue class using a list
    """

    def __init__(self):
        self.items = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.items.append(x)

    def pop(self):
        """
        :rtype: int
        """
        return self.items.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.items[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.items

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()