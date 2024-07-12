class Solution:
    def check(self, nums: List[int]) -> bool:

        for i in range(len(nums)):
            left = nums[:i]
            right = nums[i:]

            arr = right + left

            result = self.CheckSort(arr)
            if result == True:
                return True
        return False        

    def CheckSort(self, nums):
        sort = True
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                sort = False
                break
        return sort         
        