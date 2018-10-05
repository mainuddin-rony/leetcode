# Problem Link: https://leetcode.com/problems/palindrome-number/description/
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if str(x) == str(x)[::-1]:
            return 
        else:
            return "false"


x = 10
sol = Solution()
print(sol.isPalindrome(x))