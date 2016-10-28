"""
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

Subscribe to see which companies asked this question

https://leetcode.com/problems/integer-to-roman/


Symbol	I	V	X	L	C	D	M
Value	1	5	10	50	100	500	1,000



Number	    4	9	40	90	400	900
Notation	IV	IX	XL	XC	CD	CM
"""


def intToRoman(self, num):
    """
    :type num: int
    :rtype: str
    """
    dict = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

    ret = ''
    for i in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
        ret += (num // i) * dict[i]
        num -= (num // i) * i

    return ret
