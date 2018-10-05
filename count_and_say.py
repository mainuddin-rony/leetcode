#Problem Link: https://leetcode.com/problems/count-and-say/description/
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        mapper = {
            1: '1',
            2: '11',
            3: '21',
            4: '1211'
        }

        if n <= 4:
            return mapper[n]

        for m in range(5,n+1):
            prev = mapper[m-1]
            count_say = ""
            skip = 0
            for char in range(len(prev)):
                count = 1
                char = char + skip
                if char < len(prev):
                    nxt_idx = char + count
                    prev_size = len(prev)
                    if nxt_idx < prev_size:
                        while prev[char] == prev[char + count]:
                            count += 1
                            if char + count >= prev_size:
                                break

                        count_say += str(count) + str(prev[char])
                        skip += count - 1
                    else:
                        count_say += str(count) + str(prev[char])

            mapper[m] = count_say

        return mapper[n]

n = 5
sol = Solution()
print(sol.countAndSay(n))