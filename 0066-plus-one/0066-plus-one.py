class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1

        while i >= 0:
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
            i -= 1

        # If the loop completes, that means all digits were 9
        return [1] + digits

        ## First approch
        # num = int("".join(map(str,digits))) + 1
        # n = [int(i) for i in str(num)]
        # return n
