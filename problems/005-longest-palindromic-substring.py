class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

    def checkPalindrome(self, s, start, end):
        L,R = start,end
        while L>=0 and R<len(s) and s[L]==s[R]:
            L-=1
            R+=1

