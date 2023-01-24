"""The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows.

Example...
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
"""

def convert(s: str, numRows: int) -> str:
    if numRows == 1: return s # case one row
    
    rows={}
    for x in range(1,numRows+1):
        rows[f'r{x}']=[]

    i,down=1,True
    for char in s:
        rows[f'r{i}'].append(char)
        i = i+1 if down else i-1
        down = not down if i==numRows or i==1 else down

    res = ''
    for row in rows.values():
        res+= ''.join(row) 

    return res
