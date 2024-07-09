class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        val = 0
        for i in nums:
            if i in dic.keys():
                dic[i] += 1
            else:
                dic[i] = 1
                
        for key ,value in dic.items():
            if value > len(nums)/2:
                val = key
        return val        

        