class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        ## Optimized using one pass Dutch Flag

        low = mid = 0
        high = len(nums)-1

        while mid <= high:
            if nums[mid] == 0:
                nums[low],nums[mid] = nums[mid] ,nums[low]
                low +=1
                mid +=1
            elif nums[mid] == 1:
                mid +=1
            else:
                nums[mid] ,nums[high] = nums[high] ,nums[mid]
                high -= 1        
      


        # ## Brute Force Method

        # zero = nums.count(0)
        # one = nums.count(1)
        # two = nums.count(2)

        # num = ([0]*zero) + ([1]*one) + ([2]*two)
        # nums[:] = num[:]
        # return nums

       




        