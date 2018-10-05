# Problem Link: https://leetcode.com/problems/longest-common-prefix/discuss/169481/Is-the-following-expected

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        match = ""
        if len(strs) == 0:
            return match
        if len(strs[0]) == 0:
            return match
        mnm = min([len(x) for x in strs])

        for i in range(mnm):
            flag = True
            for j in range(1, len(strs)):
                flag = flag and strs[0][i] == strs[j][i]
                if not flag:
                    return match
                else:
                    continue
            match = match + strs[0][i]

        return match


strs = ["flower","flow","flight"]
sol = Solution()
print(sol.longestCommonPrefix(strs))