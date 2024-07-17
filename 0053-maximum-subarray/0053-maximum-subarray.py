class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        ## Brute force approch
        total = float("-inf")
        
        for i in range(len(nums)):
            sum = 0
            for j in range(i ,len(nums)):
                sum += nums[j]
                if sum > total:
                    total = sum
        return total           



        