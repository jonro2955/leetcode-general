class MyCircularDeque(object):
    """ https://leetcode.com/problems/design-circular-deque/

    A typical array-based deque's front side is the right side.

    Sample input sequence:
    [MyCircularDeque(3), insertLast(1), insertLast(2), insertFront(3), insertFront(4),
    getRear(), isFull(), deleteLast(), insertFront(4), getFront()]

    Expected Output:
    [null, true, true, true, false,
    2, true, true, true, 4]

    My plan is to start with an empty list. The state at each input will be:
    [] # MyCircularDeque(3), will create an empty list and a size variable equal to 3
    [1] # insertLast(1), True
    [2,1] # insertLast(2), True
    [2,1,3] # insertFront(3), True
    [2,1,3] # cannot insertFront(4) because it's full, False
    [2,1,3] # getRear(), 2
    [2,1,3] # isFull(), True
    [1,3] # deleteLast(), True
    [1,3,4] insertFront(4), True
    [1,3,4] getFront(), 4
    """

    def __init__(self, k):
        """
        :type k: int
        """
        self.items = []
        self.size = k

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        else:
            self.items.append(value)
            return True

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        else:
            self.items.insert(0, value)
            return True

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        else:
            self.items.pop()
            return True

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        else:
            self.items.pop(0)
            return True

    def getFront(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.items[-1]

    def getRear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.items[0]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return len(self.items) == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return len(self.items) == self.size

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()