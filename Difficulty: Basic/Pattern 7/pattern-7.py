#User function Template for python3

class Solution:
    def printTriangle(self, N):
        
        for row in range(N):
            for i in range(0,N - row - 1):
                print(" ", end  = "")
                
            for j in range(2*row + 1):
                print("*" , end = "")
            print()    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends