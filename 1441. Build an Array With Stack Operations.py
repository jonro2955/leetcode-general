class Solution(object):
    def buildArray(self, target, n):
        """ https://leetcode.com/problems/build-an-array-with-stack-operations/
        :type target: List[int]
        :type n: int
        :rtype: List[str]

        Note the constraints:
        1 <= target.length <= 100
        1 <= n <= 100
        1 <= target[i] <= n
        Target is strictly increasing.

        Since "target" is strictly increasing, the last number is the largest.

        We loop through the range of integers 1 upto the largest number of target,
        its last. And at each iteration, we first append the string "Push" into the
        output_list just to start. In that the same iteration, if the current integer
        is not in the "target" list, then immediately append the string "Pop" into the
        output_list, then move onto the next iteration. When all iterations are finished,
        return the output_list.

        Time complexity: O(n)
        """
        output_list = []
        for i in range(1, target[-1] + 1):
            output_list.append("Push")
            if i not in target:
                output_list.append("Pop")
        return output_list
        """
        # Alternate version: Create an empty list called "output" and iterator variable
        # initialized to 1.  
        # For each number n in "target", extend (concatenate) the output with 
        # ["Push","Pop"] * (n - iterator) + ["Push"]
        # this ensures that the correct sequence of pushes and pops are stored
        # in the output that is returned

        iterator = 1
        output = []
        for n in target:
            output.extend(["Push","Pop"] * (n - iterator) + ["Push"])
            iterator = n + 1
        return output
        """