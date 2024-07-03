#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        if N >= 1 and N<= 20:
            for row in range(1,N+1):
                for col in range(row):
                    print(row ,end = " " )
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