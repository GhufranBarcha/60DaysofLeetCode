class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        ## Optimal 
        currentSum = 0
        maxSum = float("-inf")

        for x in nums:
            currentSum = max(x ,currentSum + x)
            maxSum = max(currentSum ,maxSum)
        return maxSum    
       
        # ## Brute force approch(Time limit exceeded)
        #   total = float("-inf")
        
        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i ,len(nums)):
        #         sum += nums[j]
        #         if sum > total:
        #             total = sum
        # return total         



        