class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 2 and k > len(nums):
            nums[0],nums[1]=nums[1],nums[0]
        else:    
            mid = len(nums) - k
            nums[:] = nums[mid:] + nums[:mid]
        # for _ in range(k):
        #     nums = self.rotate1(nums)

        
    # def rotate1(self,nums):
    #         temp = nums[len(nums)-1]
    #         for i in range(len(nums) -1 ,0,-1):
    #             print(i)
                
    #             print("temp",temp)
    #             nums[i] = nums[i-1]
                
    #         nums[0] = temp 
    #         return nums
       



        