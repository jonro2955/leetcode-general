class FreqStack(object):
    """
    https://leetcode.com/problems/maximum-frequency-stack/
    My initial independently developed solution below has been effective for 33/38 test
    cases, but it gives TLE. The googled solution below it is much better.
    """

    def __init__(self):
        self.items = []
        self.frequencies = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.items.append(val)
        self.frequencies.append({"val": val, "freq": self.items.count(val)})

    def pop(self):
        """
        :rtype: int
        """
        popIndex = -1
        mostFreq = self.frequencies[popIndex]
        for i in range(len(self.frequencies) - 2, -1, -1):
            if self.frequencies[i]["freq"] > mostFreq["freq"]:
                mostFreq = self.frequencies[i]
                popIndex = i
        self.frequencies.pop(popIndex)
        return self.items.pop(popIndex)


# tests and expected behaviours:
stack = FreqStack()
stack.push(5)  # stack is [5]
stack.push(7)  # stack is [5,7]
stack.push(5)  # stack is [5,7,5]
stack.push(7)  # stack is [5,7,5,7]
stack.push(4)  # stack is [5,7,5,7,4]
stack.push(5)  # stack is [5,7,5,7,4,5]
print(stack.pop())  # prints 5
print(stack.items)  # stack is [5,7,5,7,4]
print(stack.pop())  # prints 7
print(stack.items)  # stack is [5,7,5,4]
print(stack.pop())  # prints 5
print(stack.items)  # stack is [5,7,4]
print(stack.pop())  # prints 4
print(stack.items)  # stack is [5,7]

"""
Alternate solution (Much better):

Defaultdict is a modified variation of dict. While dict will throw a KeyError if you try to get 
an item with a key that is not currently in the dictionary, defaultdict will simply create some 
"default" item for the searched key if it does not exist yet. The argument that you pass into the 
constructor determines the kind of default objects it creates. For example, defaultdict(int) will 
return the integer object: 0. defaultdict(list) will return a new empty list object: [].

class FreqStack:

    def __init__(self):
        self.freqStack = defaultdict(list)
        self.valFreq = defaultdict(int)
        self.maxFreq = 0

    def push(self, val):
        self.valFreq[val] += 1
        currFreq = self.valFreq[val]
        self.maxFreq = max(self.maxFreq, currFreq)
        self.freqStack[currFreq].append(val)
        print(self.freqStack)

    def pop(self):
        popValue = self.freqStack[self.maxFreq].pop()
        self.valFreq[popValue] -= 1
        if not self.freqStack[self.maxFreq]:
            self.maxFreq -= 1
        return popValue
"""























