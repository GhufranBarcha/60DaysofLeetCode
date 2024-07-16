class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        ## Brute force approch 
        ## just sort the array and find the middle point

        nums.sort()
        n = nums[len(nums)//2]
        return n

        ## Boyer-Moore Majority voting algorith

        n = 0
        count = 0

        for num in nums:
            if count == 0:
                n = num
            elif n != num:
                count -=1   

        return n        




















        # count = 0
        # candidate =0

        # for num in nums:
        #     if count == 0:
        #         candidate = num

        #     if num == candidate:
        #         count+=1
        #     else:
        #         count -=1
        # return candidate                
        

        