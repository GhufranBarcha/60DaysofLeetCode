#User function Template for python3

class Solution:
    def factorialNumbers(self, n):
        factorial = 1
        arrFact = []
        
        if n == 0 or n == 1:
            return [1]
        else:
            for  i in range(1, n+1):
                factorial*=i
                if factorial > n:
                    break
                else:
                    arrFact.append(factorial)
            return arrFact        
                
                
                
            
            
    	#code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorialNumbers(N)
        for i in ans:
            print(i, end=" ")
        print()

# } Driver Code Ends