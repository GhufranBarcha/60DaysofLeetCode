#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        count = 0
        
        for i in str(N):
            n_int = int(i)
            
            if n_int != 0 and N % n_int == 0:
                count+=1
        return count        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends