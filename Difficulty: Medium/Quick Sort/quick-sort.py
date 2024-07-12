#User function Template for python3

class Solution:
    def quickSort(self,array,low,high):
        # code here
        
        if low < high:
 
            pi = self.partition(array, low, high)
     
            self.quickSort(array, low, pi - 1)
     
            self.quickSort(array, pi + 1, high)
        
        
        
    
    def partition(self,array,low,high):
        
        pivot = array[high]
        i = low - 1
     
        for j in range(low, high):
            
            if array[j] <= pivot:
     
                i = i + 1
     
                (array[i], array[j]) = (array[j], array[i])
                
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        
        return i + 1   
                
                
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends