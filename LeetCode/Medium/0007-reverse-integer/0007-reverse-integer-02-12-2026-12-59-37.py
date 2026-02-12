## The easy solution is converting to string then reversing it and then multiplying it with negative

class Solution:
    def reverse(self, x: int) -> int:
        sign = 1

        if x < 0:
            sign *= -1

            x *= sign
            x = int(str(x)[::-1])
            num = sign * x
            if num > (-2)**31 and num  < (2)**31 -1:
                return num
            else: 
                return 0    
        else:
            num = int(str(x)[::-1])
            if num > (-2)**31 and num  < (2)**31 -1:
                return num
            else: 
                return 0 
  




        