class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
     
        num = int(n ** 0.5)
        if (num ** 2) == n:
            return True
        else:
            return False    
        