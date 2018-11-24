class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dct = {}

        for s in strs:
            key = ''.join(sorted(s))
            if key in dct:
                dct[key].append(s)
            else:
                dct[key] = [s]
        return list(dct.values())

