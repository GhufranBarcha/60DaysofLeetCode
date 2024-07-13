from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        st = set()
        for i in range(len(nums)):
            st.add(nums[i])
        k = len(st)
        j = 0
        for x in st:
            nums[j] = x
            j += 1
        return k

        return k    
