class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        output = -1
        l = len(needle)
        for i in range(len(haystack) - l + 1):
            if needle == haystack[i:i+l]:
                return i
        return -1        
        