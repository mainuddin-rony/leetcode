class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <=2:
            if s[::-1] == s:
                return s
            else:
                return s[0]
        max_str = s[0]
        if s[::-1] == s:
            return s
        for i in range(0, len(s)):
            for j in range(len(s), -1, -1):
                if s[i:j][::-1] == s[i:j] and len(s[i:j]) > 1:
                        max_str = s[i:j] if len(s[i:j]) > len(max_str) else max_str
        return max_str
