class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        R_cont = []
        L_cont = []
        for ch in s:
            if ch == 'R':
                R_cont.append(ch)
            else:
                L_cont.append(ch)
            if len(R_cont) == len(L_cont):
                count += 1
                R_cont = []
                L_cont = []
        return count
        
