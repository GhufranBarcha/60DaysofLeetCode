class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        max_c = 0
        cons = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                cons +=1
            else:
                if cons > max_c:
                    max_c = cons
                cons = 0

        if cons > max_c:
                max_c = cons        
        return max_c
                            


        