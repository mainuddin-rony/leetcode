#Problem Link: https://leetcode.com/problems/search-insert-position/description/

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        try:
            idx = nums.index(target)
            return idx
        except ValueError as ex:
            for i in range(len(nums)):
                if nums[i] > target:
                    return i
            return len(nums)


nums = [1,3,5,6]
target = 5
sol = Solution()
print(sol.searchInsert(nums, target))