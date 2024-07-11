#User function Template for python3

class Solution:
    # def merge(self,arr, l, m, r): 
        # code here
    def mergeSort(self,arr, l, r):
        
        if len(arr) > 1:
            
            
        
            left_arr = arr[0:len(arr)//2]
            right_arr = arr[len(arr)//2:]
            
            ## Recursion
            self.mergeSort(left_arr ,l ,r)
            self.mergeSort(right_arr,l,r)
            
            
            
            ##
            i = 0
            j = 0
            k = 0
            
            while i < len(left_arr) and j < len(right_arr):
                
                if left_arr[i] < right_arr[j]:
                    
                    arr[k] = left_arr[i]
                    i+=1
                else:
                    arr[k] = right_arr[j]
                    j+=1
                
                k +=1
                
                
            while i < len(left_arr):
                arr[k] = left_arr[i]
                i+=1
                k+=1
                
            while j< len(right_arr):
                arr[k] = right_arr[j]
                j+=1
                k+=1
            
            return arr    
        
        
        
        
        
        #code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3


import sys
input = sys.stdin.readline
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().mergeSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends