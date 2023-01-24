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
# # Another Solution
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         longest=''
#         for i in range(len(s)):
#             for j in range(len(s),i,-1):
#                 sub= s[i:j]
#                 if len(longest) >= j-i: break
#                 if sub == sub[::-1] and len(sub) > len(longest):
#                     longest = sub
#         return longest if longest else s[0]
