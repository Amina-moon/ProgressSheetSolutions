class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index=0
        counter = 0
        unique_chars = ''
        for i in range(len(s)):
            if s[i] not in  unique_chars:
                unique_chars += s[i]
                counter = max(counter , len(unique_chars))
            else:
                index += unique_chars.index(s[i]) + 1
                unique_chars = s[index:i+1]
        return counter
        
