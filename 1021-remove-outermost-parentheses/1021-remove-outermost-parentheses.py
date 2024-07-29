class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        count = 0
        for char in s:
            if char == "(":
                if count > 0:
                    result.append(char)
                count +=1
            else:
                count -= 1
                if count > 0:  
                    result.append(char)   
        return "".join(result)            

        ## My solution
        # left_paran = 0
        # right_paran = 0
        # count = []
        # st = []

        # for index,i in enumerate(s):
        #     if left_paran == right_paran:
        #         left_paran = 0
        #         right_paran = 0
        #         count.append(index)
        
        #     if i == "(":
        #         left_paran +=1
        #     else:
        #         right_paran += 1
                
        #     if left_paran == right_paran:
        #         left_paran = 0
        #         right_paran = 0
        #         count.append(index)        
        # for index,i in enumerate(s):
        #     if index not in count:
        #         st.append(i)
                
        # st = ''.join(st)        
                
        # return st
            

        