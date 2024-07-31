class Solution:
    def largestOddNumber(self, num: str) -> str:
        val = ""
        max_int = 0

        for i in num:
            val = val + i
            if int(val) % 2 != 0:
                max_int = max(int(val),max_int)
             
        if str(max_int) == "0":
            return ""
        return str(max_int)    
          
        return str(max_int)

          

                
            
                      
        