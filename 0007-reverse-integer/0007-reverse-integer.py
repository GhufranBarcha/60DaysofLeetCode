class Solution:
    def reverse(self, x: int) -> int:
        if x <= -2**31 or x>= 2**30:
            return 0
        if x >= 0:
            str_x = str(x)
            str_x = str_x[::-1]
            return int(str_x)
        else:
            x = abs(x)
            str_x = str(x)
            str_x = str_x[::-1]
            return int(str_x)*(-1)

        