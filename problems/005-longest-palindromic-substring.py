class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or s is "" or s is " " or len(s)<=1:
            return s

        it = 0
        start = 0
        length = 0

        while it < len(s)-1:
            length1 = self.checkPalindrome(s,it,it)
            length2 = self.checkPalindrome(s,it,it+1)

            if length1>length or length2>length:
                if length1>length2:
                    length = length1
                else:
                    length = length2
                start = it - ((length-1)//2)
            it+=1

        return (s[start:length+start])



    def checkPalindrome(self, s, start, end):
        L,R = start,end
        while L>=0 and R<len(s) and s[L]==s[R]:
            L-=1
            R+=1
        return (R-L-1)


