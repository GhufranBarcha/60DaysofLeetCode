class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        result = True
        index = 0
        if len(s) == 1: 
            if s not in t:
                 return False
        for i in s:
            if not result:
                return False
            result = False

            for j in range(index ,len(t)):
                if t[j] == i:
                    index = j
                    result = True
                    break

        return True      
        