class Solution:
    def myAtoi(self, str: str) -> int:
        valid_starts = ["-", ' ', '+', "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        str = str.strip()
        if len(str) > 0:
            if str[0] not in valid_starts:
                return 0
            valid_number = str[0]
            for char in str[1:]:
                if char not in valid_starts[3:]:
                    break
                else:
                    valid_number += char
            print(valid_number)
            if len(valid_number) == 1 and (valid_number == "-" or valid_number == "+"):
                return 0
            converted = int(valid_number)
            if converted < (-2**31):
                return -2**31
            if converted > (2**31 - 1):
                return 2**31 - 1
            return converted
        else:
            return 0
