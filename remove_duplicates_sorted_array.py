class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        m = 0
        for i in range(len(nums)):
            i = i-m
            if i <= len(nums) - 1:
                if i-1 >= 0:
                    if nums[i] == nums[i-1]:
                        nums.remove(nums[i])
                        m += 1
        return len(nums)


nums = [1,1,2]
sol = Solution()
print(sol.removeDuplicates(nums))