"""Given a string s, find the length of the longest substring without repeating characters. 

Example...
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest =0
        for i in range(len(s)):
            sub=s[i]
            for char in s[i+1:]:
                if char in sub:
                    break
                else:
                    sub+= char
            if len(sub) > longest:
                longest = len(sub)
        
        return longest
