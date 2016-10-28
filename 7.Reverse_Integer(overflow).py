"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Subscribe to see which companies asked this question

when overflow, back to 0
https://leetcode.com/problems/reverse-integer/
"""
def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    neg = False
    if x < 0:
        neg = True

    x = ''.join(str(abs(x)))
    x = x[::-1]

    if neg:
        x = '-' + x

    x = int(x)
    if x > 2147483647 or x < -2147483647:
        return 0

    return x
