class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        middle =  len(s) // 2
        length = len(s) - 1

        l_s = list(s)

        for x in range(middle):
            l_s[x], l_s[length - x] = l_s[length - x], l_s[x]

        s = ''.join(l_s)
        return s

#
#   super easy solution using python slices
#   return s[::-1]
#

