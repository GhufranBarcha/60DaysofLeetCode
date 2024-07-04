class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < -2**31 or x > 2**31-1:
            return 0

        if str(x) == str(x)[::-1]:
            return True
        else:
            return False 

        