class MyCircularQueue(object):
    """ https://leetcode.com/problems/design-circular-queue/

    Using a python list to implement the circular queue, the left end will be the front,
    the right end will be the rear.
    """

    def __init__(self, k):
        """
        :type k: int

        The self.rear index number will be 1 place ahead of the last item in self.items list,
        and it signifies the place where the next enqueue will occur, but only if it is less
        than the size, k. This is what makes the queue circular. The front will be the first
        item of the list, so there is no need to create a variable to track it.
        """
        self.items = []
        self.size = k
        self.rear = 0

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool

        Enqueues will append to the list from the right.
        """
        if self.rear < self.size:
            self.items.append(value)
            self.rear += 1
            return True
        else:
            return False

    def deQueue(self):
        """
        :rtype: bool

        A dequeue will shift all values to the left one spot, then pop the right-most item. It
        should ideally save the left-most item before shifting and return it, but the problem
        requires that we simply remove it and return a boolean.
        """
        if self.items:
            for i in range(1, len(self.items)):
                self.items[i - 1] = self.items[i]
            self.rear -= 1
            self.items.pop()
            return True
        else:
            return False

    def Front(self):
        """
        :rtype: int
        """
        return self.items[0] if self.items else -1

    def Rear(self):
        """
        :rtype: int
        """
        return self.items[-1] if self.items else -1

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

    # Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()