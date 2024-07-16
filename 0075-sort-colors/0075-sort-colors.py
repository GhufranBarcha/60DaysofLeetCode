class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        ## Brute Force Method

        zero = nums.count(0)
        one = nums.count(1)
        two = nums.count(2)

        num = ([0]*zero) + ([1]*one) + ([2]*two)
        nums[:] = num[:]
        return nums

       




        