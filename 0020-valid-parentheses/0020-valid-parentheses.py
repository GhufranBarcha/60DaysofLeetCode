class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1 or s[0] in [")","]","}"]: return False
        stack = []
        j = ""
        inc = 0
        for i in s:
            if i==")":
               j = "("
            if i == "}":
               j = "{"
            if i == "]":
                j = "["   

            if i == "(" or i == "{" or i == "[":
                stack.append(i)
                inc+=1
            else:
                inc -= 1
                if stack[-1] == j:
                    stack.pop()
                else:
        
                    return False
                    
        if inc == 0:
            return True
        else: 
            return False                       

        ## Using stack

        # inc1 = 0
        # inc2 = 0
        # inc3 = 0
        # for i in range(len(s)):
        #     if s[i] == "(":
        #         inc1 +=1
        #     elif s[i] == "{":
        #         inc2 += 1
        #     elif s[i] == "[":  
        #         inc3 += 1  

        #     elif s[i] == ")":
        #         inc1 -=1
        #     elif s[i] == "}":
        #         inc2 -= 1
        #     elif s[i] == "]":  
        #         inc3 -= 1              
            
                

        # if inc1 == 0 and inc2 == 0 and inc3 == 0:
        #     return True
        # else:
        #     return False           




        ## Failed for some cases
        # ret = True
        # for i in range(len(s)-1):
        #     if s[i] == "(":
        #         if s[i+1] != ")":
        #             ret = False
        #     if s[i] == "[":
        #         if s[i+1] != "]":
        #             ret = False      
        #     if s[i] == "{":
        #         if s[i+1] != "}":
        #             ret = False  
        # return ret             
