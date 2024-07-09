class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        

        
        freq = {}

                # code here
        for i  in arr:
            if i in freq.keys():
                freq[i]  +=  1
            else:
                freq[i]  =  1
        
        
        arr.clear()
        for j in range(1 ,N+1):
            if j in freq.keys():
                arr.append(freq[j])
            else:
                arr.append(0)
                
        return arr       
            
                




#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__=="__main__":
	T=int(input())
	while(T>0):
		N=int(input())
		arr=[int(x) for x in input().strip().split()]
		P=int(input())
		ob=Solution()
		ob.frequencyCount(arr, N, P)
		for i in arr:
			print(i, end=" ")
		print()
		T-=1



# } Driver Code Ends