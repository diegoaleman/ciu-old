class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0
        findChar = False

        for i in range(len(s)-1,-1,-1):
            if s[i] == ' ':
                if findChar:
                    return counter
            else:
                findChar = True
                counter = counter + 1
        if findChar:
            return counter
        else:
            return 0

