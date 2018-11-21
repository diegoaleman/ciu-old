class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 1

        current_number = 0
        it = 1
        while it < len(nums):
            if nums[current_number] != nums[it]:
                current_number = it
                it = it+1
            else:
                nums.pop(it)
        return len(nums)

