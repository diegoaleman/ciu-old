# Kadane's algorithm
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_value = None
        prev_max = None

        for index, val in enumerate(nums):
            if index == 0:
                max_value = nums[0]
                prev_max = nums[0]
            else:
                if val > prev_max + val:
                    prev_max = val
                else:
                    prev_max = prev_max + val

                max_value = max(max_value,prev_max)

        return max_value

sol = Solution()
print(sol.maxSubArray([1]))

