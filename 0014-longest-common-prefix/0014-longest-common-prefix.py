class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        switch = True
        value = 0
        for char in range(len(strs[0])):
            value = char
            for word in range(len(strs)):
                if strs[0][char] != strs[word][char]:
                    switch = False
                    break
            if not switch:
                break
        return strs[0][:value]        


                   

                    
            

        