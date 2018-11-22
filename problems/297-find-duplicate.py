# This problem can be solved in three ways
# 1. Sorting the list and then searching for duplicates (next to each other)
# 2. Creating a set and checking if current number is already in set
# 3. Using Floyd's runner technique
#    L The list can be represented as a list with a cycle

class Solution:
    # METHOD 1
    def findDuplicate1(self, nums):
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]

    # METHOD 2
    def findDuplicate2(self, nums):
        s = set()
        for x in nums:
            if x in s:
                return x
            else:
                s.add(x)

    # METHOD 3
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[slow]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

