# Problem Link: https://leetcode.com/problems/roman-to-integer/description/
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapper = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

        if len(s) == 1:
            return mapper[s]
        int_sum = 0
        inc = 0
        for i in range(len(s)):
            i += inc
            if i <= len(s) - 1:
                consd = s[i: i+2]
                if consd in mapper:
                    int_sum += mapper[consd]
                    inc += 1
                else:
                    int_sum += mapper[s[i]]

        return int_sum



s = "LVIII"
sol = Solution()
print(sol.romanToInt(s))