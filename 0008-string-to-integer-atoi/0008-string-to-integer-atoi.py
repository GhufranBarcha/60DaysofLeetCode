class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if s == "":
            return  0
        start = None
        result = 0
        if s[0] == "+" or s[0] == "-":
            start = s[0]
            s = s[1:]

        for i in range(1,len(s)+1):
            try:
               result = int(s[0:i])
               
            except:
                break
        if result > 2**31 - 1:
            result = 2**31        

        if start != None:
            if start == "-":
                result = -1 * result
                return result
            else:
                return result
        return result        

     





        # sign = None



        # if s[0] == "+" or s[0] == "-":
        #     sign = s[0]
        # num = None    

        # for i in range(1 ,len(s)):
        #     if s[i] == type("int"):
        #         if s[i] == 0 and num is not None:
        #             num = 0
        #             return num


            
        