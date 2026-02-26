class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        count = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                count += 1
                if i == len(nums) - 1:
                    if max_count < count:
                        max_count = count                 
            else:
                if max_count < count:
                    max_count = count
                count = 0
        return max_count        


            
        