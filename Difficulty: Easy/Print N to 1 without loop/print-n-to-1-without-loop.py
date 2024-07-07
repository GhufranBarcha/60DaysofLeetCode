#User function Template for python3

class Solution:
    def printNos(self, n):
        
            
            # Code here
        def recursionRev(N):
                
            print(N ,end = " ")
            if N ==1:
                return
                
            return recursionRev(N-1)
                
        if n>= 1 and n<=1000:        
             recursionRev(n) 
        else:
            return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printNos(N)
        print()
# } Driver Code Ends