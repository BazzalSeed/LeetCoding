"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate
 the number of 1's in their binary representation and return them as an array.

 Atacched pic to see the core concept
"""


class Solution(object):

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        special = 1
        steps = 1
        res = []
        res.append(0)
        for i in xrange(1, num + 1):
            if(i == special):
                res.append(1)
                special = special << 1
                steps = 1
            else:
                res.append(res[steps] + 1)
                steps += 1
        return res
