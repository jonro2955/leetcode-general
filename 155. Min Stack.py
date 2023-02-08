class MinStack(object):
    """ https://leetcode.com/problems/min-stack/
    My initial version:
    """

    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def getMin(self):
        return min(self.items)


"""
Alternate version
    
class MinStack:

    def __init__(self):
        self.items = []

    def push(self, val):
        m = val
        if self.items:
            m = self.items[-1][1]
            if m > val:
                m = val
        self.items.append((val, m))

    def pop(self):
        return self.items.pop()
        
    def top(self):
        return self.items[-1][0]

    def getMin(self):
        return self.items[-1][1]
        
"""