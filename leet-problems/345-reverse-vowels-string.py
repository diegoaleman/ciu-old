class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_s = list(s)
        init = 0
        end = len(list_s) - 1

        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        while init < end:
            while (init < end) and (list_s[init] not in vowels):
                init+=1

            while (init < end) and (list_s[end] not in vowels):
                end-=1

            if init < end:
                list_s[init], list_s[end] = list_s[end], list_s[init]
                init+=1
                end-=1

        return ''.join(list_s)

