class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        i = len(digits) - 1
        for i in range(len(digits)-1 , -1 ,-1):
            if digits[i] != 9:
                digits[i] += 1
                break
            elif digits[i] == 9:
                digits[i] == 0
            elif digits[i] == 9 and i == 0:
                digits[i] == 1
                digits.append(0)

        if len(digits) == 1:
            if digits[0] == 9:
                digits[0] = 1
                digits.append(0)
            else:
                digits[0] += 1    
        return digits        
        


        ## First approch
        # num = int("".join(map(str,digits))) + 1
        # n = [int(i) for i in str(num)]
        # return n