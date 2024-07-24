class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) -1

        if target == 0 and nums[0] > 0:
            return 0

        while low <= high:
            mid = (low + high)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1    

        return mid + 1           
        