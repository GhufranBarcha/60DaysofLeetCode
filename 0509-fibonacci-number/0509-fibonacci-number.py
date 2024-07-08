class Solution:
    def fib(self, n: int) -> int:
        def fibna(n):
            if n == 1:
                return 1
            if n == 0:
                return 0  

            return fibna(n-1) + fibna(n-2)

        if n>=0 and n<=30:
            return fibna(n)  
        else: return -1      


        