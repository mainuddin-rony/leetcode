#problem link: https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            int_str = ""
            flag = True
            idx = len(str(x)) - 1
            if len(str(x)) == 1:
                return x
            while flag:
                int_str += str(x)[idx]
                idx -= 1
                if idx < 0:
                    flag = False

            if int(int_str) < (2**31):
                return int(int_str)
            else:
                return 0

        else:
            int_str = ""
            flag = True
            x = x * (-1)
            idx = len(str(x)) - 1
            if len(str(x)) == 1:
                return x
            while flag:
                int_str += str(x)[idx]
                idx -= 1
                if idx < 0:
                    flag = False
            conv_int = int(int_str) * (-1)
            if conv_int > -(2**31)-1:
                return int(int_str) * -1
            else:
                return 0


sol = Solution()
x = 10
print(sol.reverse(x))
