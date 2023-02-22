class Solution(object):
    def isValid(self, s):
        """ https://leetcode.com/problems/valid-parentheses/
        :type s: str
        :rtype: bool
        """
        stack=[]
        lefts="({["
        rights=")}]"
        for ch in s:
            if ch in lefts:
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                elif stack.pop() != lefts[rights.index(ch)]: # key is to get the index from rights
                    return False
        return not stack



