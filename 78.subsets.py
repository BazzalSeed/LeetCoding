"""
Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution(object):

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        position = 0
        result, branch = [], []
        length = len(nums)
        self.dfs(position, branch, sorted(nums), length, result)
        return result

    def dfs(self, position, branch, nums, length, result):
        result.append(branch)
        for i in xrange(position, length):
            self.dfs(i + 1, branch + [nums[i]], nums, length, result)
