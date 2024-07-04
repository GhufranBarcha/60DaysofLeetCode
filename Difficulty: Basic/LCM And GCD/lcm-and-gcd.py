 
        
class Solution:
    #User function Template for python3
    def gcd(self,A,B):
        
        while B > 0:
            r = A%B
            A = B
            B = r
        return A  
 
    def lcmAndGcd(self, A , B):
        
        if A <= 1 or B <=1:
            return -1
        g = self.gcd(A,B)
        lcm = (A*B)//g
        
        return [lcm ,g]
        # code here 
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
# } Driver Code Ends