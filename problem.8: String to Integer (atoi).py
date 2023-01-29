"""
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
# Constraints:
// 0 <= s.length <= 200
// s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.

Notes: 
= if the first thing to read, other than ' ', is a character or '.', stop reading and return 0. 
= the string should not have addition or subtraction operations inside, otherwise the return is 0. 
"""
def myAtoi(self, s: str) -> int:
    s=s.lstrip()
    if len(s)==0: return 0
    if s[0].isdigit() or s[0] in ['+','-']:
        negative, positive, number = False,False, ""
        readingBegan= True
        for char in s:
            if char.isalpha(): break
            if char == '.' or char == ' ': break                   
            elif char == '-' or char == '+' or char.isnumeric():
                if char == '-': 
                    if not len(number) > 0:
                        if positive or negative: break
                        else: negative = True
                    else: break
                if char == '+': 
                    if not len(number)>0:
                        if negative or positive: break
                        else: positive = True
                    else: break
                if char.isnumeric(): number += char

        if len(number)!=0:
            if negative: number = -int(number)
            else: number = int(number)


            if number in range(-2**31, 2**31):
                return number
            elif number < (-2**31):
                return -2**31
            else:
                return (2**31)-1
        else: return 0
    else:
        return 0
