class Solution:
    def isDuplicate(result,l):
        pass


    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = set()
        dct = {}
        triple_zero = False

        for i in range(len(nums)-2):
            target = -1 * nums[i]
            if triple_zero and target is 0:
                continue
            for j in range(i+1, len(nums)):
                val = target - nums[j]
                if val in dct:
                    a = nums[i]
                    b = nums[dct[val]]
                    c = nums[j]
                    l = [a,b,c]
                    l.sort()
                    if l == [0,0,0]:
                        triple_zero = True
                    result.add(tuple(l))
                else:
                    dct[nums[j]] = j
            dct.clear()
        result = list(result)

        return list(map(lambda x:list(x),result))


