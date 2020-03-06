class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        
        for idx in range(len(nums) - 2):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            
            left = idx + 1
            right = len(nums) - 1
            
            while left < right:
                # print("Trying for ", nums[idx], nums[left], nums[right])
                total = nums[idx] + nums[left] + nums[right]
                if total < 0:
                    left = left + 1
                elif total > 0:
                    right = right - 1
                else:
                    results.append([nums[idx], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left+1]:
                        left = left + 1
                    while left < right and nums[right] == nums[right -1]:
                        right = right -1
                        
                    left += 1
                    right -= 1
        return results
            
        
