class Solution:
    #Back-end complete function Template for Python 3
    
    
    #Function to find the leaders in the array.
    def leaders(self,n, arr):
        
        arr1= []
        max_element = float("-inf")
        
        
        for i in range(n-1 , -1 ,-1):
            if arr[i] >= max_element:
                arr1.append(arr[i])
                max_element = arr[i]
                
                
        return arr1[::-1]        

                
        
      
            
            
             
            

                
   
                
                
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():

    T = int(input())

    while (T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        obj = Solution()

        A = obj.leaders(N, A)

        for i in A:
            print(i, end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends