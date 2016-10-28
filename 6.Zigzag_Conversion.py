"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
Subscribe to see which companies asked this question


https://leetcode.com/problems/zigzag-conversion/
"""

def convert(self, s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1:
        return s
    A = [[] for i in range(numRows)]
    B = list(range(numRows)) + list(range(numRows - 2, 0, -1))
    r = 2 * numRows - 2
    j = 0
    for i, c in enumerate(s):
        i = i % r
        A[B[i]].append(c)
    res = []
    for i in range(numRows):
        res.extend(A[i])
    return ''.join(res)
