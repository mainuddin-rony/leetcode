class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        if len(haystack) < len(needle):
            return -1

        return haystack.find(needle)


haystack = "mississippi"
needle = "issip"
sol = Solution()
print(sol.strStr(haystack, needle))