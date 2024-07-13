class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 2 and k > len(nums):
            nums[0] ,nums[1]=nums[1],nums[0]
        else:    
            mid = len(nums) - k
            arr = nums[mid:] + nums[:mid]

            for i in range(len(nums)):
                nums[i] = arr[i]
        