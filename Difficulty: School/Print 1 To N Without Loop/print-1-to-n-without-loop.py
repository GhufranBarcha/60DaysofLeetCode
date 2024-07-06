#User function Template for python3

class Solution:    
    #Complete this function
    
    def printNos(self,N):
        if N>= 1 and N<=1000:
            
            count = 0
            def recursion(n ,c):
                     
                if n == 0:
                    return
                else:
                            
                    c+=1
                    print(c ,end = " ")
                           
                    return recursion(n-1 ,c)
            recursion(N, count) 
            
        else:
            return -1
                
        
        #Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math




def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        ob=Solution()
        
        ob.printNos(N)
        print()
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends