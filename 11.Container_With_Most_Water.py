"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines,
which together with x-axis forms a container, such that the container contains the most water.
https://leetcode.com/problems/container-with-most-water/
"""


def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    start, end = 0, len(height) - 1
    max_area = 0
    max_indexes = [0, 0]
    while (start != end):
        cur_area = (end - start) * min(height[start], height[end])
        if cur_area > max_area:
            max_area = cur_area
            max_indexes = [start, end]
        if height[end] > height[start]:
            start += 1
        else:
            end -= 1
    return max_area
