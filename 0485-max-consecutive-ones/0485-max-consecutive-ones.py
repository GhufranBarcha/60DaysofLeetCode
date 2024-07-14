class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        max_c = 0
        cons = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                cons += 1
                max_c = max(cons , max_c)
            else:
                cons = 0
        return max_c
