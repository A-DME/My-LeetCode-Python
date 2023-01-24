"""Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned)."""

def reverse(self, x: int) -> int:
        while str(x)[-1] == '0' and len(str(x))> 1: x//=10
        res = int(str(x)[::-1]) if x>=0 else -int(str(x)[::-1][:-1])
       
       if res in range((-2)**31,(2**31)-1):
            return res
        else:
            return 0
