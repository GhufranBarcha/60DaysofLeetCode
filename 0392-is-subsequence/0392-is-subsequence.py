class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0

        for i in s:
            found = False

            while index < len(t):
                if t[index] == i:
                    found = True
                    index +=1
                    break
                index+=1
            if not found:
                return False
        return True                

 
        