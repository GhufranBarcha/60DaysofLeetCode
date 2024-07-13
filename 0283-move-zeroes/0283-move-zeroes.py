class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < len(nums): 
        # for i in range(len(nums)):
            if nums[i] == 0:
                for j in range(i,len(nums)-1):
                    nums[j+1],nums[j] = nums[j] ,nums[j+1]
            if nums[i]==0:
                for j in range(i,len(nums)-1):
                    nums[j+1],nums[j] = nums[j] ,nums[j+1]

            i+=1        

                 
                    
        