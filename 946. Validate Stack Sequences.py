class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """

        """
        Sample input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]

        Start by processing each item i in the "popped" list from left to right. 
        Let "push_index_i" represent the index number of item i in the "pushed" list.
        As we process each i, if i has a value after it, we'll call it "next_pop" 
        "next_pop" must be in the following list of "allowable next pops":

        allowed_pops = pushed[ push_index_i - 1 ] + pushed[ push_index_i + 1: ] 

        In other words, the next popped item has to be either the left side neighbour of 
        the item i in the "pushed" array, or it has to be one of the items pushed in 
        after it. We cannot pop any values that are burried in the middle of the stack 
        without popping other additional items first. 

        If next_pop is not contained in the allowed_pops values, then return false. 
        If next_pop is contained in the allowed_pops values, then pop the current 
        item i from the "pushed" list and iterate.
        """

        for i in range(len(popped)):
            current_pop = popped[i]
            next_pop = None
            if i < len(popped) - 1:
                next_pop = popped[i + 1]
            push_index_i = pushed.index(current_pop)
            allowed_pops = [pushed[push_index_i - 1]]
            if push_index_i < len(pushed) - 1:
                allowed_pops += pushed[push_index_i + 1:]
            if next_pop is None:
                return current_pop in allowed_pops
            else:
                if next_pop in allowed_pops:
                    pushed.pop(push_index_i)
                else:
                    return False

        """
        # alternate version
        
        stack = []
        i = 0
        for num in pushed:
            stack.append(num) # push the number to the stack
            while len(stack) > 0 and stack[len(stack) - 1] == popped[i] :
                # if the last item of stack is equal to popped[i]
                stack.pop()
                i += 1 #we are incrementing i
        return True if len(stack) == 0 else False
        """
