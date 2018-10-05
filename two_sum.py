# Problem link: https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            rem = target - nums[i]
            try:
                idx = nums.index(rem)
                if i != idx:
                    return [i, idx]
                else:
                    continue
            except ValueError as exp:
                continue
        return []


sol = Solution()
nums = [2, 7, 11, 15]
target = 9
print(sol.twoSum(nums, target))