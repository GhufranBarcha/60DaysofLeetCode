class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ## Trying optimal way( Does't work as we cant modify array)
        numMap = {}
        n = len(nums)

        for i in range(n):
            numMap[nums[i]] = i

        ## Find the complement:

        for i in range(n):
            result = target - nums[i]
            if result in numMap and numMap[result] != i:
                return [i, numMap[result]]  
      



       ## Initial Brute Force approch (Works)
        # for i in range(len(nums)):

        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return[i,j]

        