# Problem Link: https://leetcode.com/problems/valid-parentheses/description/
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapper = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        if len(s) == 0:
            return True
        run_list = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                run_list.append(s[i])
            else:
                if len(run_list) > 0 and run_list.pop() == mapper[s[i]]:
                    continue
                else:
                    return False
        if len(run_list) == 0:
            return True
        else:
            return False



s = "{[]}"
sol = Solution()
print(sol.isValid(s))