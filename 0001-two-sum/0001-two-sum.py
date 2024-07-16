class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ## Trying optimal way( Does't work as we cant modify array)
        num = sorted(nums)
        i = 0
        j = 1
        store = [1 ,1]

        while True:
            if num[j] > target:
                i = None
                j = None
                break
            if num[i] + num[i+j] > target:
                j+=1
                i = 0
            if num[i]+num[i+j] == target:
                print(i ,i+j)
                break

            i+=1
            
        first = True
            
        for f in range(len(num)):
            if num[i] == nums[f] and first:
                first = False
                store[0] = f
            if num[i+j] == nums[f]:
                store[1] = f   

        return store       



       ## Initial Brute Force approch (Works)
        # for i in range(len(nums)):

        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return[i,j]

        