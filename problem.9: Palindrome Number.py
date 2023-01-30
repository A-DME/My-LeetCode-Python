""" 
Given an integer x, return true if x is a palindrome, and false otherwise.
Constraint: -2^31 =< x < 2^31
"""

def isPalindrome(self, x: int) -> bool:
    if x in range((-2**31),2**31):
        return str(x) == str(x)[::-1]
