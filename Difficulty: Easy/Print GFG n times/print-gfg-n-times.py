#User function Template for python3

class Solution:
    def printGfg(self, n):
        if  n>= 1 and n<=1000:
            
        
            def recursionLoop(n):
                
                if n == 0:
                    return
                
                print("GFG" ,end = " ")
                
                return recursionLoop(n-1)
                
            recursionLoop(n)
            
        else:
            return -1
        # Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printGfg(N)
        print()
# } Driver Code Ends