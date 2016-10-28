"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

'1': '*',
'2': 'abc',
'3': 'edf',
'4': 'ghi',
'5': 'jkl',
'6': 'mno',
'7': 'pqrs',
'8': 'tuv',
'9': 'wxyz',
'0': ' '

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

"""


class Solution(object):

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        result = []
        length = len(digits)
        self.dfs(0, "", result, digits, length)
        return result

    def dfs(self, position, branch, res, digits, length):
        num_dict = {
            '1': '*',
            '2': 'abc',
            '3': 'edf',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' '}
        if position == len(digits):
            res.append(branch)
            return
        for char in num_dict[digits[position]]:
            new_branch = branch + char
            self.dfs(position + 1, new_branch, res, digits, length)
