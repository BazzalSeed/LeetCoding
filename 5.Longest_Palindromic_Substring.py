"""
Dynamic Solution
buiild table where table[i][j] true iff when substring (i,j) is a palindrotic
https://leetcode.com/problems/longest-palindromic-substring/
"""


def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    if (len(s) <= 1):
        return s
    maxlen = 1
    dp = [[False for x in range(len(s))] for y in range(len(s))]
    longest = ""
    for l in xrange(len(s)):
        for i in range(len(s) - l):
            j = i + l
            if(s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1])):
                dp[i][j] = True
                if (j - i + 1 > maxlen):
                    maxlen = j - i + 1
                    longest = s[i:j + 1]
    return longest
