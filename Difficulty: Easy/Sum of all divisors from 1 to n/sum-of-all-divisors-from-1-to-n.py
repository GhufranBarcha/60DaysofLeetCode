#User function Template for python3


class Solution:
    def sumOfDivisors(self, N):
        if N >=1 and N<=10**6: 
        
            sum = 0
        	#code here 
        	for i in range(1,N+1):
        	   k = N//i
        	   sum += i* k
        	return sum 
        else: return -1
    	    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sumOfDivisors(N)
        print(ans)
# } Driver Code Ends