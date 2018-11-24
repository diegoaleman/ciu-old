#
#This problem has two well known solutions:
#    1. O(n^3) solution by iterating over each of the chars in the string
#       and and count unique chars to the right of it
#
def lengthOfLongestSubstring2(self, s):
    char_set = set()
    current_max = 0
    for x in range(len(s)):
        for y in range(x,len(s)):
            if s[y] in char_set:
                current_max = max(len(char_set), current_max)
                char_set.clear()
                char_set.add(s[y])
                current_max = max(len(char_set), current_max)
                char_set.clear()

        return current_max

#   2. O(n) solution by having two pointers in the string (sliding window)
class Solution:
    def lengthOfLongestSubstring(self,s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        dct = {}
        current_max = 0

        for index, letter in enumerate(s):
            if letter in dct and dct[letter] >= start:
                current_max = max(index-start, current_max)
                start = dct[letter] + 1
            dct[letter] = index
        return max(current_max, len(s) - start)

