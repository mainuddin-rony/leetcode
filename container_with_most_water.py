class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) -1
        results = []
        
        if len(height) == 2:
            return min(height[0], height[1])
        
        while start != end:
            if height[start] > height[end]:
                results.append(height[end] * (end-start))
                end -= 1
            else:
                results.append(height[start] * (end-start))
                start += 1
        return max(results)
