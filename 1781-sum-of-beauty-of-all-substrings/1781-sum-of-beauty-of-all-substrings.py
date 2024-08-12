from collections import Counter
class Solution:
    def beautySum(self, s: str) -> int:
        sum = 0
        for i in range(len(s)):
            for j in range(i ,len(s)+1):
                if len(s[i:j]) > 2:
                    char_count = Counter(s[i:j])
                    max_char = max(char_count.values())
                    min_char = min(char_count.values())
                    sum += max_char - min_char
        return sum    
              




        