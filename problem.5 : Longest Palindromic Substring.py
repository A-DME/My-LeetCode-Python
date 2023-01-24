"""Given a string s, return the longest palindromic substring in s.

Example...
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
 """
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest=''
        for i in range(len(s)):
            sub=s[i]
            for j in range(i+1,len(s)):
                sub+= s[j]
                if sub == sub[::-1] and len(sub) > len(longest):
                    longest = sub
        return longest if longest else s[0] # as s maybe contains no palindromic substrings / very few chars
