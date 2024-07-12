#User function Template for python3
class Solution:
    def print2largest(self, arr):
            # Code Here
            
            if len(arr) == 1:
                return -1
                
            else:
                largest = -1
                second = -1
    
                for num in arr:
                    if num > largest:
    
                       
                        second = largest
                        largest = num
                    elif num < largest and num > second and num != largest:
                        second = num
                        
                return second 
               
                    
                    

                       
                    
                


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.print2largest(arr)
        print(ans)

# } Driver Code Ends