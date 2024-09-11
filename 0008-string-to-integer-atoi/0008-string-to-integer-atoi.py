class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """ 
        s = s.strip()
        if s == "":
            return 0

        start = None
        result = 0

        if s[0] == "+" or s[0] == "-":
            start = s[0]
            s = s[1:]

        for i in range(1 , len(s) + 1):
            try:
                if start != None:
                    result = int(start + s[0:i])
                else:
                    result = int(s[0:i])  
            except:
                break   
                 
        if result < -2**31 and start != None:
            result = -2**31
            return result  
        if result > 2**31 - 1:
            result = 2**31 - 1
            return result              
        return result             










            
        