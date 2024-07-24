#User function Template for python3

class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        
        # code here
        floor = float("inf")
        ceil = -1
        
        for i in arr:
            if i <= x:
                ceil= max(i , ceil)
            if i >= x:
                floor = min(floor ,i)
        
        if floor == float("inf"):
            floor = -1
                
        return [ceil ,floor]        
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        x = int(input())
        arr = list(map(int, input().split()))

        ob = Solution()
        ans = ob.getFloorAndCeil(x, arr)
        print(ans[0], ans[1])


if __name__ == "__main__":
    main()

# } Driver Code Ends