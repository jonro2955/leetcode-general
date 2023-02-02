class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool

        Start by processing each item current_pop in the "popped" list from left to right.
        Let push_index represent the index number of current_pop in the "pushed" list.
        As we process each current_pop, if there is a value after it in the "popped" list,
        we'll call it next_pop. next_pop must be in the following list:

        allowed_pops = pushed[ push_index - 1 ] + pushed[ push_index + 1: ]

        This means that the next popped item has to be either the left neighbour of
        the current_pop in the "pushed" array, or it has to be one of the items pushed
        after it in the "pushed" array. We cannot pop any values that are burried in the
        middle of the stack without popping other items first.

        If next_pop is not found in the allowed_pops list, then return false.
        If it is found, then pop current_pop from the "pushed" list and continue iterating.
        If there is no next_pop because we are at the last item in "popped" list, then
        return true if current_pop is in allowed_pops, or false otherwise.
        """
        for i in range(len(popped)):
            current_pop = popped[i]
            next_pop = None
            if i < len(popped) - 1:
                next_pop = popped[i + 1]
            push_index = pushed.index(current_pop)
            allowed_pops = [pushed[push_index - 1]]
            if push_index < len(pushed) - 1:
                allowed_pops += pushed[push_index + 1:]
            if next_pop is None:
                return current_pop in allowed_pops
            else:
                if next_pop in allowed_pops:
                    pushed.pop(push_index)
                else:
                    return False
        """
        # Alternate version: for each num in pushed, push num into our own stack,
        # and right after pushing, pop them off if the popped list has a matching 
        # value in the correct order. At the end, there should be nothing left in
        # the stack.

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
























