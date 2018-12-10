class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {'{':'}', '[':']', '(':')'}

        for x in s:
            if x in dict:
                stack.append(x)
            else:
                if len(stack) is 0:
                    return False
                pop = stack.pop()
                if dict.get(pop) is not x:
                    return False
        if len(stack) > 0:
            return False
        else:
            return True

