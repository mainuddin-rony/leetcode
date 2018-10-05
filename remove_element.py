class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return len(nums)
        if len(nums) == 1:
            if nums[0] == val:
                return 0
            else:
                return 1

        m = 0
        for i in range(len(nums)):
            i = i-m
            if i <= len(nums) - 1:
                if nums[i] == val:
                    nums.remove(nums[i])
                    m += 1
        return len(nums)

nums = [0,1,2,2,3,0,4,2]
val = 2
sol = Solution()
print(sol.removeElement(nums,val))