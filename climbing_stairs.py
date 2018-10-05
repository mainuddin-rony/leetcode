# Problem Link: https://leetcode.com/problems/climbing-stairs/description/

class Solution:
    def factorial(self,n):
        num = 1
        while n >= 1:
            num = num * n
            n = n - 1
        return num

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        total = 0
        for m in range(int(n/2)+1):
            num_2 = m
            num_1 = n - m *2
            total += (self.factorial(num_1 + num_2)/(self.factorial(num_1) * self.factorial(num_2)))

        return int(total)



n = 5
sol = Solution()
print(sol.climbStairs(n))