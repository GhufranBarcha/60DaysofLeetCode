class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1 = dict()
        dict2 = dict()

        for i in s:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1 

        for i in t:
            if i in dict2:
                dict2[i] += 1
            else:
                dict2[i] = 1 

        if sorted(dict1.values()) == sorted(dict2.values()):  
            return True
        else:
            return False                  