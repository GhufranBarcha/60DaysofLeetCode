class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        maxV = 1
        for i in range(0 ,x//2 + 1):
            if i**2 <= x:
                maxV= max(i , maxV)
            else:
                break
        return maxV            


        