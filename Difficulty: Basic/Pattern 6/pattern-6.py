#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        
        for row in range(1,N+1):
            for col in range(1 , N + 2 - row):
                print(col, end = " ")
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