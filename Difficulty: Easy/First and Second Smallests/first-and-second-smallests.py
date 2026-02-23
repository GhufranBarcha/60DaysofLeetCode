class Solution:
    def minAnd2ndMin(self, arr):

        if len(arr) <= 1:
            return [-1]        
        
        first = float('inf')
        second = float('inf')
        
        for num in arr:
            
            if num < first:
                second = first
                first = num
                
            elif first < num < second :
                second = num
        if second == float('inf'):
            return [-1]
                
                
        return [first, second]       
                