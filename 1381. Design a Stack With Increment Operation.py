class CustomStack(object):
    
    """
    My version: beats about 32% of cases in both measurements
    """

    def __init__(self, maxSize):
        self.items = []
        self.maxSize = maxSize

    def push(self, x):
        if len(self.items) < self.maxSize:
            self.items.append(x)

    def pop(self):
        if not self.items:
            return -1
        elif len(self.items) > 0:
            return self.items.pop()

    def increment(self, k, val):
        for i in range(k):
            if i < len(self.items):
                self.items[i] += val

    """
    Alternate version below beats about 92% of cases in both measurements.
    It uses an additional array "inc" to record the increment value,
    where inc[i] means for all elements items[0] ~ items[i],
    and we add inc[i] to the items when they are popped - we don't add things 
    to items when the increment(k,val) method is called.
    Then inc[i-1]+=inc[i], so that we can accumulate the increment inc[i]
    for the bottom elements and the following pops.

    Complexity:
    Initialization, push, pop, increment, all O(1) time and space.
    """

    """
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.items = []
        self.inc = []

    def push(self, x):
        if len(self.inc) < self.maxSize:
            self.items.append(x)
            self.inc.append(0)

    def pop(self):
        if not self.inc: return -1
        if len(self.inc) > 1:
            self.inc[-2] += self.inc[-1]
        return self.items.pop() + self.inc.pop()

    def increment(self, k, val):
        if self.inc:
            self.inc[min(k, len(self.inc)) - 1] += val
    """

