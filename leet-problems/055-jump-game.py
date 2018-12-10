class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target = len(nums)-1
        stack = [0]
        visited = set()
        while len(stack) > 0:
            current_index = stack.pop()
            visited.add(current_index)
            if current_index == target:
                return True

            if current_index > target:
                continue

            if nums[current_index] > 0:
                for i in range(1,nums[current_index]+1):
                    val = current_index + i
                    if val not in visited:
                        stack.append(current_index+i)
        return False
