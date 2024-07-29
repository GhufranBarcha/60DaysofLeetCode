class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        left_paran = 0
        right_paran = 0
        count = []
        st = []

        for index,i in enumerate(s):
            if left_paran == right_paran:
                left_paran = 0
                right_paran = 0
                count.append(index)
        
            if i == "(":
                left_paran +=1
            else:
                right_paran += 1
                
            if left_paran == right_paran:
                left_paran = 0
                right_paran = 0
                count.append(index)        
        for index,i in enumerate(s):
            if index not in count:
                st.append(i)
                
        st = ''.join(st)        
                
        return st
            

        