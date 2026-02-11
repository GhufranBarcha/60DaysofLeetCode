class Solution:
    def isPalindrome(self, x: int) -> bool:
        pal = str(x) == str(x)[::-1]
        return pal
        