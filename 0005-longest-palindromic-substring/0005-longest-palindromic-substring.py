class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        resN = 0

        for i in range(len(s)):
            r,l = i ,i

            while l >= 0 and r < len(s) and s[r] == s[l]:
                if (r - l + 1) > resN:
                    res = s[l:r+1]
                    resN = r - l + 1
                l -= 1
                r += 1

            r,l = i+1 ,i

            while l >= 0 and r < len(s) and s[r] == s[l]:
                if (r - l + 1) > resN:
                    res = s[l:r+1]
                    resN = r - l + 1
                l -= 1
                r += 1
                    
        return res


        ##Brute force works
        # maxstring = ""

        # for i in range(len(s)):
        #     for j in range(i,len(s)+1):
        #         string = s[i:j]
                
        #         if string == string[::-1]:
        #             if len(string) >= len(maxstring):
        #                 maxstring = string

        # return maxstring                
        