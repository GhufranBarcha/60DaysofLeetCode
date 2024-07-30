class Solution:
    def reverseWords(self, s: str) -> str:
        strng = ""
        lastWord = ""
        spaceFirst = True
        for char in s.strip():
            

            if char != " ":
                lastWord = lastWord + char
                spaceFirst = True
            else:
                if spaceFirst:
                    strng =  lastWord + " " + strng
                    lastWord = ""
                    spaceFirst = False
            
        strng =  lastWord + " " + strng 
        return strng.strip()


        