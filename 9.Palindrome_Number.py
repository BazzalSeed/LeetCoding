"""
Determine whether an integer is a palindrome. Do this without extra space.

Approach:
reverse and check
"""


class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return self.reverse_number(x) == x

    def reverse_number(self, number):
        s = str(abs(number))
        news = []
        for i in s:
            news.insert(0, i)
        return int(''.join(news))
