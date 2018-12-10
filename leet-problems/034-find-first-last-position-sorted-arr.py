class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(nums)-1
        found = False

        while start<=end and not found:
            middle = (start+end)//2
            if target > nums[middle]:
                start = middle + 1
            elif target < nums[middle]:
                end = middle - 1
            else:
                start,end = middle,middle
                found = True

        if not found:
            return [-1,-1]
        else:
            while start-1 >=0 and nums[start-1] == target:
                start-=1
            while end+1 <= len(nums)-1 and nums[end+1] == target:
                end+=1

        return [start,end]

