class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < -2**31 or x > 2**31-1:
            return 0

        if x < 0 :
            return False
        else:
            reverse = 0
            x_1 = x

            while x > 0:
                reverse = (reverse * 10 ) + (x % 10)   
                x = x // 10
            return reverse == x_1         

        if str(x) == str(x)[::-1]:
            return True
        else:
            return False 

        