class Solution:
    def reverse(self, x: int) -> int:
        val = 0

        sign = 1 if x > 0 else -1 
        x = abs(x)

        while x:

            div = x % 10
            val = (val * 10) + div
            x = x // 10


        # Apply the sign
        val *= sign
        
        # Check 32-bit overflow
        if val < -2**31 or val > 2**31 - 1:
            return 0
        
        return val

    


 










        ## Brute force approch
        # if x >= 0:
        #         num = int(str(x)[::-1])
        #         return num if num <= (2**31) and num >= -2**31 else 0
        # else:
                
        #         value = str(x)[1:]
        #         value = int(value[::-1])
        #         num = value * -1
        #         return num if num <= (2**31) and num >= -2**31 else 0



            