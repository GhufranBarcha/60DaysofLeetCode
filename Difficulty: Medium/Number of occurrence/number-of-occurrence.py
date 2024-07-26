class Solution:

    def count(self, arr, n, x):
        # code here
        
        def left(target, nums):
            low = 0
            high = len(nums) - 1
            
            while low <= high:
                mid = (low + high) // 2
                
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
                    
            return low
        
        left_index = left(x, arr)
        
        count = 0
        while left_index < n and arr[left_index] == x:
            count += 1
            left_index += 1
        
        return count

		     
		    
		
		
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends