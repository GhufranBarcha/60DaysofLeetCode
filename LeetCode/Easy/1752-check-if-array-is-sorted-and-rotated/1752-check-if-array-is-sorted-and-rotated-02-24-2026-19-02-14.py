from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:

        def sorte(arr):
            arr = arr.copy()  # avoid mutating original
            
            # Proper bubble sort
            for end in range(len(arr) - 1, 0, -1):
                swapped = False
                for j in range(end):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        swapped = True
                if not swapped:
                    break
            return arr
        
        sorted_arr = sorte(nums)

        n = len(nums)

        for _ in range(n):

            # Check before rotating
            if nums == sorted_arr:
                return True

            # Right rotation by 1
            temp = nums[-1]
            for i in range(n - 1, 0, -1):
                nums[i] = nums[i - 1]
            nums[0] = temp

        return False