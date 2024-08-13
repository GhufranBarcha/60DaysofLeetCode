class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        output = -1
        l = len(needle)
        for i in range(len(haystack)):
            if needle == haystack[i:i+l] and (i+l) <= len(haystack):
                output = i
                break
        return output        
        