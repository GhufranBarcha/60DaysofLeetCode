class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = -1
        h = -1

        if len(nums) == 1 and nums[0] == target:
            return [0,0]
        for i in range(len(nums) - 1):
            if  nums[i] == target:
                l = max(l , i)
                if nums[i+1] == target:
                    h = i
        return [h ,l]            
                



        