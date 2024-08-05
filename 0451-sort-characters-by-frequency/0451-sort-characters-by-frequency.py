class Solution:
    def frequencySort(self, s: str) -> str:
        dict1 = {}
        string = ""
        maxV = 0
        k = None

        for i in s:
                    if i in dict1:
                        dict1[i] += 1
                    else:
                        dict1[i] = 1 
                        
                      
        while dict1:              
                    maxV = 0
                    for key,value in dict1.items():
                        if value >= maxV:
                            maxV = value
                            k = key
                    string +=  (maxV * k)  
                    del dict1[k]   
        return string               


             






        