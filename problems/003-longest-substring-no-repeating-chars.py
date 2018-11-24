class Solution:
    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
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

    def lengthOfLongestSubstring(self,s):
        """
        :type s: str
        :rtype: int
        """

