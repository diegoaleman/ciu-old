#
# Return the index of the two numbers in the list
# that add up to the target value
#
class Solution:
    def twoSum(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}

        for x in range(len(nums)):
            if nums[x] in dict:
                return [dict.get(nums[x]), x]
            else:
                dict[target - nums[x]] = x
        return []

