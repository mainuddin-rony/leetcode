class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        stack = []
        
        if len(s) < 2:
            return len(s)
        
        for ch in s:
            if ch not in stack:
                stack.append(ch)
                max_len = len(stack) if len(stack) > max_len else max_len
            else:
                index = stack.index(ch)
                stack = stack[index+1:]
                stack.append(ch)
                max_len = len(stack) if len(stack) > max_len else max_len
        return max_len
