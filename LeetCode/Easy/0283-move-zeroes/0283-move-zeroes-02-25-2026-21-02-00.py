class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # arr = []
        # count = 0
        # for i in nums:
        #     if i == 0:
        #         count += 1
        #     else:
        #         arr.append(i)
        # nums[:] = arr + [0] * count
        # return nums     

        i = 0
        j = 0

        while j < len(nums) - 1:

            if nums[i] == 0 and nums[j] == 0:
                j += 1
            if nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j],nums[i]
                i += 1
  







        